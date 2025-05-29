from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    starting_price = models.IntegerField()
    url = models.URLField(blank=True) # optional
    category = models.CharField(max_length=20, null=True) 
    
    watcher = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="watched_listings",
        blank=True)
    
    is_closed = models.BooleanField(default = False)
    
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "listings"
        )
    
    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = "won_item")

    final_price = models.IntegerField()
    
    @property
    def current_bid(self):
        return self.bid_item.order_by('-bid').first()

    @property
    def current_price(self):
        if self.is_closed and self.final_price is not None:
            return self.final_price
        top = self.current_bid
        return top.bid if top else self.starting_price

    @property
    def current_winner(self):
        if self.is_closed:
            return self.winner
        top = self.current_bid
        return top.bidder if top else None

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_item")
    bid = models.IntegerField()
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bidder_for_the_listing") 

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item_for_comment")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter") 
    body = models.CharField(max_length=300)

