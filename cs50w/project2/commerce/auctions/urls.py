from django.urls import path

from . import views

urlpatterns = [
    path("create", views.create, name="create"),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<str:item>", views.item, name="item")
]
