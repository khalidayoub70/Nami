# views.py
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login as auth_login  
import requests
from django.http import JsonResponse

from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render

from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect

from .models import  UserProfile



def get_token(request):
    if request.method == 'POST':
        auth_url = "https://api-staging.namipay.com.sa/client/get_token"
        data = {
            "grant_type": "client_credentials",
            "client_id": "merchantapp",
            "client_secret": "r4vKbc17kVdKtC8R5jCvQZkgXyICRnW0",
            "scope": "SCOPE_MERCHANTAPP"
        }
        headers = {"Accept": "application/json"}

        response = requests.post(auth_url, data=data, headers=headers)

        if response.status_code == 200:
            token_data = response.json()
            return JsonResponse(token_data)
        else:
            return JsonResponse({"error": "Authentication failed"}, status=400)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)



def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('number')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname, password=password)
        my_user.save()
        print(uname, password)
        return redirect('login')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('number')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            #login(request,user)
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('authorized')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'authorized.html',{})

def home (request):
    return render(request,'home.html')

def submit_work(request):
    interns = Intern.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect or display a success message
            return HttpResponseRedirect('/success/')
    else:
        form = TaskForm()
        print('internlist',interns)
    
    return render(request, 'home.html', {'form': form, 'interns': interns})
def Success(request):
    # return HttpResponse('<b>Hello Interns<b>')
    return render(request, 'success.html')


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

