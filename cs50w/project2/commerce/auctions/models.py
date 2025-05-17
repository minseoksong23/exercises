from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title=models.CharField(max_length=150)
    image
    created #datetime?

class Bid
    listing=models.ForeignKey(Listing, on_delete-models.CASCADE, related_name="bid item")
    bidder #among users?
    amount
    placed_at #datetime?

class Comment(models.Model):
    listing
    author
    body=
    posted_at #datetime?
