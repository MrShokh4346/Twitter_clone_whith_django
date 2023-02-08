from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles':profiles})
    else:
        messages.info(request, 'You must be logged in')
        return redirect('home')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(id=pk)
        return render(request, "Profile.html", {'profile':profile})
    else:
        messages.info(request, 'You must be logged in')
        return redirect('home')