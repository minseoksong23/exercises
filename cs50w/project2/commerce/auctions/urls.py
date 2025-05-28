from django.urls import path

from . import views

urlpatterns = [
    path("create", views.create, name="create"),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("togglewatch", views.togglewatch, name="togglewatch"),
    path("bid", views.bid, name="bid"),
    path("item/<int:item_id>", views.item, name="item"),
    path("close/<int:listing_id>", views.close_listing, name="close_listing")
]
