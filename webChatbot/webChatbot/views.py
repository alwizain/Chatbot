from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm


@login_required(login_url='/login')
def index(request):
	context = {
		'subjudul' : "Dashboard",
	}

	return render(request,'index.html',context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('indexuser')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('indexuser')
            else:
            	messages.error(request, 'username and password doesn\'t match')

    return render(request, 'login.html')



@login_required(login_url='/login')
def signout(request):
    logout(request)
    return redirect('login')	


def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'register.html', {"form": form})