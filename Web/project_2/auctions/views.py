from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from auctions.forms import CreateListingForm, BidForm, CommentForm

from .models import Category, Listing, User


def index(request):
    active_listings = Listing.objects.filter(is_active=True)
    for listing in active_listings:
        listing.current_price = get_current_price(listing)
    return render(request, "auctions/index.html", {"active_listings": active_listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == "POST":
        form = CreateListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect("view_listing", listing_id=listing.id)
        return render(request, "auctions/create_listing.html", {"form": form})

    form = CreateListingForm()  
    return render(request, "auctions/create_listing.html", {"form": form})


def get_current_price(listing):
    highest_bid = listing.bids.order_by("-amount").first()
    return highest_bid.amount if highest_bid else listing.starting_bid


def view_listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    current_price = get_current_price(listing)
    watched = (
        request.user.is_authenticated and 
        listing in request.user.watchlist.all()
    )

    context = {
        "listing": listing,
        "current_price": current_price,
        "bids_count": listing.bids.count(),
        "watched": watched,
        "comments": listing.comments.order_by("-created_at"),
        "bid_form": BidForm(),
        "comment_form": CommentForm()
    }

    return render(request, "auctions/view_listing.html", context)


@login_required
def toggle_watch(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    user = request.user

    if user.watchlist.filter(pk=listing_id).exists():
        user.watchlist.remove(listing)
        messages.success(request, "Listing removed from your watchlist.")
    else:
        user.watchlist.add(listing)
        messages.success(request, "Listing added to your watchlist.")
    
    return redirect("view_listing", listing_id=listing_id)
    

@login_required
def place_bid(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    if not listing.is_active:
        messages.error(request, "Listing is closed.")
        return redirect("view_listing", listing_id=listing_id)

    form = BidForm(request.POST)

    if not form.is_valid():
        messages.error(request, "Invalid input.")
        return redirect("view_listing", listing_id=listing_id)
            
    bid_amount = form.cleaned_data["amount"]
    highest_bid = listing.bids.order_by("-amount").first()

    if highest_bid:
        if bid_amount <= highest_bid.amount:
            messages.error(request, f"Bid must be greater than current price of ${highest_bid.amount}.")
            return redirect("view_listing", listing_id=listing_id)
    else:
        if bid_amount < listing.starting_bid:
            messages.error(request, f"Bid must be at least the starting bid of ${listing.starting_bid}.")
            return redirect("view_listing", listing_id=listing_id)
    
    bid = form.save(commit=False)
    bid.listing = listing
    bid.bidder = request.user
    bid.save()
    messages.success(request, "Bid placed successfully.")
       
    return redirect("view_listing", listing_id=listing_id)


@login_required
def add_comment(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.listing = listing
        comment.author = request.user
        comment.save()
        messages.success(request, "Comment added successfully.")
    return redirect("view_listing", listing_id=listing_id)



@login_required
def close_listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    if request.user != listing.owner:
        messages.error(request, "Only the owner can close this listing.")
        return redirect("view_listing", listing_id=listing_id)
    
    if not listing.is_active:
        messages.error(request, "Listing is already closed.")
        return redirect("view_listing", listing_id=listing_id)

    highest_bid = listing.bids.order_by("-amount").first()

    listing.winner = highest_bid.bidder if highest_bid else None
    listing.is_active = False
    listing.save()
    messages.success(request, "Listing closed.")

    return redirect("view_listing", listing_id=listing_id)



def view_categories(request):
    categories = Category.objects.all()
    
    return render(request, "auctions/categories.html", {"categories": categories})


def category_listings(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    category_active_listings = Listing.objects.filter(category=category, is_active=True)
    
    return render(request, "auctions/category_listings.html", {
                "category_active_listings": category_active_listings, 
                "category": category
                })

@login_required
def watchlist(request):
    watchlist_listings = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html", {"watchlist": watchlist_listings})
