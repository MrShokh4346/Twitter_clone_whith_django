from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Post
from .forms import PostForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.info(request, 'You have been loged in')
            return redirect('home')
        else:
            messages.info(request, 'Login was failde.Try again...')
            return redirect('login')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been loged out')
    return redirect('home')

def index(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.info(request, 'Successfully posted')
                return redirect('home')
        posts = Post.objects.all().order_by('-created')
        return render(request, "index.html", {'posts':posts, 'form':form})
    else:
        posts = Post.objects.all().order_by('-created')
        return render(request, "index.html", {'posts':posts})

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
        posts = Post.objects.filter(user_id=pk)
        if request.POST.get('follow') == 'follow':
            request.user.profile.follows.add(profile)
        elif request.POST.get('follow') == 'unfollow':
            request.user.profile.follows.remove(profile)
        
        return render(request, "Profile.html", {'profile':profile, "posts":posts})
    else:
        messages.info(request, 'You must be logged in')
        return redirect('home')