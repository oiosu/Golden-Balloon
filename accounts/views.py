from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from email import message
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def mypage_1(request, pk):
    user = get_user_model().objects.get(pk=pk)

    context = {
        'user': user,
    }
    return render(request, 'accounts/mypage_1.html', context)

def mypage_2(request, pk):
    user = get_user_model().objects.get(pk=pk)

    context = {
        'user': user,
    }
    return render(request, 'accounts/mypage_2.html', context)

@login_required
def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        messages.warning(request, '스스로 팔로우 할 수 없습니다.')
        return redirect('accounts:mypage_2', pk)

    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)

    return redirect('accounts:mypage_2', pk)

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:mypage_1', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)