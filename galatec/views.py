from django.contrib.auth import (
    authenticate,
    login, logout,
)
from .forms import UserLoginForm, UserForm
from django.shortcuts import render
from .models import UserTable
from django.utils import timezone


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


def login_user(request):
    username = 'not logged in'

    if request.method == 'POST':
        myloginform = UserLoginForm(request.POST)
        if myloginform.is_valid():
            username = myloginform.clean_message()
            request.session['username'] = username
            request.session.set_expiry(60*60*24)
    else:
        myloginform = UserLoginForm()

    return render(request, 'user_home.html', {'username': username})


def forget_view(request):
    title = 'Forgot Password'
    return render(request, 'forget.html', {'title': title})


def logout_view(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return render(request, 'index.html', {})
    # logout(request)
    # form = UserLoginForm(request.POST or None)
    # context = {
    #     "form": form,
    # }



def register_view(request):
    title = 'Register Here'
    return render(request, 'registration.html', {'title': title})


def create_user(request):
    if request.method == 'POST':
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
            err_msg = 'User Created, Login'
            return render(request, 'login.html', {'username': username, 'password': password, 'err_msg': err_msg})
        else:
            err_msg = 'Fill required Fields Correctly'
            return render(request, 'registration.html', {'err_msg': err_msg})