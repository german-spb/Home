from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

def home(request):
    return render(request, 'home.html')

def counters(request):
    return render(request, 'counters.html'                  )