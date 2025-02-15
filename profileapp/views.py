from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profileapp/profile.html', {'profile': profile})