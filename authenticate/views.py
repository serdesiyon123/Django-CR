from django.shortcuts import render, redirect
from .forms import UserRegister
from django.contrib.auth import login, logout,authenticate

import logging

logger = logging.getLogger(__name__)

def signup_form(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect ('/home')
        else:
            logger.error(f'Form is not valid: {form.errors}')
    elif request.method == 'GET':
        form = UserRegister()
    return render(request, 'registration/signup.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('/login')







# def login_form(request):
#     if request.method == 'POST':
#        form = UserRegister(request.POST)
#        if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request,user)
#             return redirect('/home')
#     elif request.method == 'GET':
#       form = UserRegister()
#
#
#     return render(request,'auth/login.html', {'form': form })



def redirect_login(request):
    return redirect('/login')