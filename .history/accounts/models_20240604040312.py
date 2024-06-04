from django.db import models
from django.contrib.auth.models import User


class USerProfile(models.Model):
    profileName=models.OneToOneField(User,on_delete=models.CASCADE)
    profilePicture=models.ImageField(upload_to="accouts/",default="C:\Users\Vijay\django_pro\hotels\static\image\profile\userprofile.jpg")
    dateOfBirth=models.DateTimeField()
    city=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.profileName
    
    
    
     