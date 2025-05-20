from django.contrib.auth import authenticate, login, logout
from django import forms
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Listing, Bid, Comment 

class ListingForm(forms.Form):
    title = forms.CharField(label="listing", required=False)
    description = forms.CharField(label="description", required=False)
    starting_bid = forms.IntegerField(label="starting_bid", required=False)
    url = forms.URLField(label="url", required=False)
    category = forms.CharField(label="category", required=False) 

class CommentForm(forms.Form):
    body = forms.CharField(label="body", required=False)

class WatchForm(forms.Form):
    watch = forms.CharField(label="watch", required=False)

def create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            Listing.objects.create(
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                starting_bid = form.cleaned_data["starting_bid"],
                url = form.cleaned_data["url"],
                category = form.cleaned_data["category"]
            )
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html")  

def watchlist(request):
    if request.method == "POST":
        form = WatchForm(request.POST)
        if form.is_valid():
            #lst = Listing.objects.filter(title=request.POST.get("title")).first()
            lst = get_object_or_404(Listing, title=request.POST.get("title"))
            lst.watcher.add(request.user)
    return render(request, "auctions/watchlist.html",{ 
        "watchlists": request.user.watched_listings.all()
    })

def item(request, item):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                listing = Listing.objects.filter(title=item).first(),
                commenter = request.user, 
                body = form.cleaned_data["body"]
            )
            return HttpResponseRedirect(reverse("item", args=[item]))
    return render(request, "auctions/item.html", {
        "item": Listing.objects.filter(title=item).first(),
        "comments": Comment.objects.all()
    })

def index(request):
    return render(request, "auctions/index.html", {
        "Listing": Listing.objects.all()        
    })


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

