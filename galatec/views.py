from django.contrib.auth import (
    authenticate,
    login, logout,
)
from .forms import UserLoginForm, UserForm
from django.shortcuts import render
from .models import UserTable
from django.utils import timezone
from gala.views import admin_index


def index(request):
    username = ''
    return render(request, 'user_home.html', {'username': username})


def about_us(request):
    return render(request, 'about_us.html', context=None)


def terms(request):
    return render(request, 'terms.html', context=None)


def faqs(request):
    return render(request, 'faqs.html', context=None)


def contact_us(request):
    return render(request, 'contact_us.html', context=None)


def chart(request):
    count = 0;
    return render(request, 'chart.html', context=None)


def test_page(request):
    return render(request, 'test_page.html', context=None)


def login_view(request):
    title = "Login Here"

    return render(request, 'login.html', {'title': title})


def create_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = request.POST['username']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        password = request.POST['password']
        conf_password = request.POST['con-password']
        date_reg = timezone.datetime.now().date()
        if password == conf_password:
            UserTable.objects.create(
                username=username,
                email=email,
                phonenumber=phonenumber,
                password=password,
                date_reg=date_reg,
            )
            success_message = 'User Created, Login'
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    context = {
                        'username': username,
                        'password': password,
                        'success_message': success_message,
                        'title': 'Login Here',
                    }
                    return render(request, 'login.html', context)
        else:
            error_message = 'Fill required Fields Correctly'
            return render(request, 'registration.html', {'error_message': error_message, 'title': 'Register Here'})
    context = {
        "form": form,
        'title': 'Register Here',
    }
    return render(request, 'registration.html', context)


def login_user(request):
    title = 'Login Here'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['username'] = username
                request.session.set_expiry(60 * 60 * 24)
                if username == 'gala_admin':
                    return render(request, 'dash.html',{})
                else:
                    return render(request, 'user_home.html', {})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled', 'title': title})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login', 'title': title})
    return render(request, 'login.html', {'title': title})


def forget_view(request):
    title = 'Forgot Password'
    return render(request, 'forget.html', {'title': title})


def logout_user(request):
    logout(request)
    form = UserLoginForm(request.POST or None)
    context = {
        "form": form,
        'title': 'Login Here'
    }
    return render(request, 'login.html', context)


def register_view(request):
    title = 'Register Here'
    return render(request, 'registration.html', {'title': title})



