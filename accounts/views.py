from django.contrib.auth import (
    authenticate,get_user_model,
    login,logout,
)
# from .forms import UserForm
from django.db.models import Q
from django.http import JsonResponse
from .forms import UserLoginForm, UserForm
# from .forms import UserForm

from django.shortcuts import render, get_object_or_404


def login_view(request):
    title = "Login Here"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html', {'title': title})


def forget_view(request):
    title = 'Forgot Password'
    return render(request, 'forget.html', {'title': title})


def logout_view(request):
    logout(request)
    form = UserLoginForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'index.html', context)


def register_view(request):
    title = 'Register Here'
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        # phone = form.cleaned_data['phone']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html', {})
    return render(request, 'registration.html', {"form": form, 'title': title})
