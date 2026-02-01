from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listings/<int:listing_id>", views.view_listing, name="view_listing"),
    path("listings/<int:listing_id>/watch", views.toggle_watch, name="toggle_watch"),
    path("listings/<int:listing_id>/bid", views.place_bid, name="place_bid"),
    path("listings/<int:listing_id>/comment", views.add_comment, name="add_comment"),
    path("listings/<int:listing_id>/close", views.close_listing, name="close_listing"),
    path("categories", views.view_categories, name="categories"),
    path("categories/<str:category_name>", views.category_listings, name="category_listings"),
    path("watchlist", views.watchlist, name="watchlist"),
]
