from django.db import models
from django.contrib.auth.models import User
from base.models import hotel
# Create your models here.
class Room(models.Model):
    id=models.UUIDField(primary_key=True,)
    hotels=models.ForeignKey(hotel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    roomName=models.CharField(max_length=100)
  hotels  roomType=models.CharField(max_length=100)
    price=models.IntegerField()
    roomImage=models.ImageField(upload_to="roomImages")
    def __str__(self) -> str:
        return self.roomName