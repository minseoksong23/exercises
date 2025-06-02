from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("like-post/<int:post_id>/", views.toggle_like, name="toggle_like"),
    path("posts/create/", views.create_post, name="create"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("edit/<int:post_id>/", views.edit, name="edit"),
    path("edit_complete", views.edit_complete, name="edit_complete"),
    path("follow", views.follow, name="follow")
]
