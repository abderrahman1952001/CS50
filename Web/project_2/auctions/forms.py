from django import forms
from .models import Listing, Category, Bid, Comment

class CreateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "starting_bid", "category", "image_url"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "starting_bid": forms.NumberInput(attrs={"class": "form-control", "step": 0.01}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image_url": forms.URLInput(attrs={"class": "form-control"})
        }

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ["amount"]
        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": 0.01})
        }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "class": "form-control"})
        }
    
