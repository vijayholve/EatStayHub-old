from django.db import models
from django.contrib.auth.models import User
from base.models import hotel
import uuid
class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
        ('5BHK', '5BHK'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    roomName=models.CharField(max_length=100)
    location=models.CharField(max_length=200,default="PUNE")
    available=models.BooleanField(default=True)
    price=models.IntegerField()
    roomImage=models.ImageField(upload_to="roomImages/",null=True,blank=True)
    roomType=models.CharField(max_length=200,choices=ROOM_TYPE_CHOICES)
    def __str__(self) -> str:
        return self.roomName

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    duration=models.IntegerField(default=1)
    def s
