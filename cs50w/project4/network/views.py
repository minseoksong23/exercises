from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator

from .models import User, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class EditForm(forms.Form):
    title=forms.CharField(label="title")
    content=forms.CharField(label="content")
    Id=forms.IntegerField(label="Id")

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    
    context = {'form': form, 'Post': posts, "page_obj": page_obj}
    return render(request, 'network/index.html', context)

def edit_complete(request):
    form = EditForm(request.POST)
    print(form.errors)
    if form.is_valid():
        post = Post.objects.get(id=form.cleaned_data["Id"])
        post.title = form.cleaned_data["title"]
        post.content = form.cleaned_data["content"]
        post.save()
        return HttpResponseRedirect(reverse("index"))
    raise Http404("error editing")

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.creator = request.user
            new_post.likes = 0
            new_post.save()
            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'network/index.html', {'form': form})

@login_required
def toggle_like(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "like":
            post.likes += 1
        elif action == "unlike":
            post.likes -= 1
        post.save()
        return JsonResponse({"likes": post.likes})
    else:
        raise Http404("Endpoint only accepts POST requests")

@login_required
def profile(request, user_id):
    user = User.objects.get(id = user_id)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "follow":
            user.followers.add(request.user)
        elif action == "unfollow":
            user.followers.remove(request.user)
        return JsonResponse({"follower_ct": user.followers.count(),
                             "following_ct": user.following.count()
                             })
    else:
        return render(request, "network/profile.html", {
            "profile_user":user,
            "followers_": user.followers.count(),
            "following_": user.following.count(),
            "Post": Post.objects.filter(creator = user)
        })

@login_required
def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.creator != request.user:
        return PermissionDenied()
    return render(request, 'network/edit.html', {
            "post":post
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        uosername = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
