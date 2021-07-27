from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator


# Create your views here.

def indexView(request):
    return render(request, 'index.html')


def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')

        else:
            messages.info(request, 'invalid username and password')
            return redirect('login_url')
    else:
        return render(request, 'registration/login.html')


@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('register_url')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register_url')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                password=password1, email=email)
                user.save()
                messages.success(request, 'Registration Successfully completed, Now please Login!')
                return redirect('login_url')
        else:
            messages.info(request, 'password not matching')
            return redirect('register_url')

        # return redirect('login_url')
    else:
        return render(request, 'registration/register.html')


def LogoutView(request):
    auth.logout(request)
    return redirect('login_url')

    # if request.method == "POST":
    #   form = UserCreationForm(request.POST)
    #  if form.is_valid():
    #     form.save()
    #    messages.success(request, 'Registration Successfully completed, Now please Login!')
    #   return redirect('login_url')
    # else:
    #   form = UserCreationForm()
    # return render(request, 'registration/register.html', {'form': form})


# def HomeView(request):
# return render(request, 'index.html')
