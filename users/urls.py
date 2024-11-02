from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, signup_success_view

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", signup_view, name="signup"),
    path("signup-success/", signup_success_view, name="signup_success"),
]
