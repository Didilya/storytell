from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.forms import UserCreationForm


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Create the user
            login(request, user)  # Log the user in
            return redirect("signup_success")  # Redirect to a success page
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


def signup_success_view(request):
    return render(request, "signup_success.html")
