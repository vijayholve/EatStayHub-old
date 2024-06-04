from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import USerProfile

def profile(request):
    userProfile=user.objects.all()
    content={"userProfile":userProfile}
    return render(request,"accounts/userProfile.html",content)