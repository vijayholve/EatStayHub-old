from django.shortcuts import render
from django.contrib.auth.models import User


class UserProfile(models.Models):
    ProfileNAme=models.fieldName = models.CharField(max_length = 150)
    