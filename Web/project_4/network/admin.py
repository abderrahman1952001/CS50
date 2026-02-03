from django.contrib import admin
from .models import User, Post, Comment, Like, Follow

for model in [User, Post, Comment, Like, Follow]:
    admin.site.register(model)

