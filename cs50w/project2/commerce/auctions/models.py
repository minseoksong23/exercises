from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    starting_bid = models.IntegerField()
    url = models.URLField(blank=True) # optional
    category = models.CharField(max_length=20, null=True) 
    watcher = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="watched_listings",
        blank=True
    )

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_item")
    bid = models.IntegerField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder_for_the_listing") 

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item_for_comment")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter") 
    body = models.CharField(max_length=300)

