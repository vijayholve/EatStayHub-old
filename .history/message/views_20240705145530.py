from django.shortcuts import render,redirect
from base.models import restaurants,dish 
from django.contrib.auth.models import User
from .models import message 
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from django.contrib import messages 
@login_required(login_url="login-page") 
def message_home(request,rest_id,user_id):
    restaurant=restaurants.objects.get(id=rest_id)
    if request.user is restaurant.user:
        sender=User.objects.get(id=user_id) 
    receiver=User.objects.get(id=user_id)  
    sender_list=message.objects.filter(Q(restaurant=restaurant)).distinct()
    message_obj=message.objects.filter(Q(restaurant=restaurant) & Q(sender=sender) &  Q(receiver=receiver))
    if request.method == "POST":
        message_text=request.POST.get("message")
        message_obj=message.objects.create(
            receiver=receiver,
            sender=sender,
            text=message_text,
            restaurant=restaurant
        )
        message_obj.save()
        return redirect("message-home",rest_id=restaurant.id)
    context={"message_obj":message_obj,"sender":sender,"receiver":receiver}
    return render(request,"message/message_home.html",context)

 
def reciever_list(request,receiver_id , sender_id):
    sender=message.objects.filter(sender__id=sender_id)
    reciever=message.