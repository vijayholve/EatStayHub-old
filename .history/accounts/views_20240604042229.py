from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import USerProfile

def profile(request):
    user=USerProfile.objects
    return render(request,"userProfile.html")