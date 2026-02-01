from django.contrib import admin
from .models import User, Listing, Bid, Comment, Category

# Register your models here.
for model in (User, Listing, Bid, Comment, Category):
    admin.site.register(model)


