from decimal import Decimal
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    watchlist = models.ManyToManyField("Listing", blank=True, related_name="watchlisted_by")

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_listings")
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, blank=True, null=True, related_name="listings")
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="won_listings")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name


class Bid(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))])
    created_at = models.DateTimeField(auto_now_add=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    
    def __str__(self):
        return f"{self.amount} on {self.listing.title} by {self.bidder}"


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment by {self.author} on {self.listing.title}"
    
    


