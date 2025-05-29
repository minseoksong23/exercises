from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Bid, Comment 

class BidForm(forms.Form):
    bid = forms.IntegerField(label='bid', required=False)

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "description", "starting_price", "url", "category")

    def clean_starting_price(self):
        bid = self.cleaned_data["starting_price"]
        if bid <= 0:
            raise forms.ValidationError("Bid must be positive")
        return bid

class CommentForm(forms.Form):
    body = forms.CharField(label="body", required=False)

class WatchForm(forms.Form):
    watch = forms.CharField(label="watch", required=False)

def create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.creator = request.user
            new_listing.final_price = new_listing.starting_price
            new_listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html")  

def category(request, category_str):
    return render(request, "auctions/index.html", {
        "Listing": Listing.objects.filter(category=category_str)        
    })

@login_required
def close_listing(request, listing_id):
    if request.method != "POST":
        raise Http404()
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.user != listing.creator:
        return HttpResponseForbidden("You cannot close this listing")

    if listing.is_closed:
        return Http404("The listing is already closed")

    listing.is_closed = True
    listing.save()
    return HttpResponseRedirect(reverse("index"))

def bid(request, item_id):
    listing = get_object_or_404(Listing, pk = item_id)
    if listing.is_closed:
        messages.error(request, "This listing is closed. No further bids are allowed")
        return redirect("item", item_id)

    if request.method == 'POST':
        form = BidForm(request.POST)

        if form.is_valid():
            bid_amount = form.cleaned_data["bid"]
            lst = Listing.objects.get(id=item_id)
            Bid.objects.create(listing=listing, bidder=request.user, bid=bid_amount)
        else:
            return render(request, "auctions/item.html", {
                "item": listing,
                "comments": listing.item_for_comment
            })

    return redirect("item", item_id)

def watchlist(request):
    return render(request, "auctions/watchlist.html",{ 
        "watchlists": request.user.watched_listings.all()
    })

def togglewatch(request):
    if request.method == "POST":
        form = WatchForm(request.POST)
        if form.is_valid(): 
            lst= get_object_or_404(Listing, id=int(request.POST.get("id")))
            if request.POST.get("add_or_remove")=="1": #add
                lst.watcher.add(request.user)
                return HttpResponseRedirect(reverse("item", args=[int(request.POST.get('id'))]))
            else:
                lst.watcher.remove(request.user)
                return HttpResponseRedirect(reverse("item", args=[int(request.POST.get('id'))]))

def item(request, item_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                listing = Listing.objects.filter(id=item_id).first(),
                commenter = request.user, 
                body = form.cleaned_data["body"]
            )
            return HttpResponseRedirect(reverse("item", args=[item_id]))
    return render(request, "auctions/item.html", {
        "item": Listing.objects.get(id=item_id),
        "comments": Comment.objects.filter(listing = Listing.objects.filter(id=item_id).first())
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

