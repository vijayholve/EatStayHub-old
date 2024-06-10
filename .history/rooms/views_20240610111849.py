from django.shortcuts import render,redirect,get_object_or_404
from .forms import room_form
from base.models import hotel
from  django.contrib import messages
from .models import Room,Booking
import re
from .seed import send_mail_to_user_after_booking
from datetime import datetime
def home_room(request):
    rooms = Room.objects.all()
    booked_rooms = []
    for room in rooms:
        try:
            Booking.objects.get(room=room)
            booked_rooms.append(room)
        except Booking.DoesNotExist:
            pass
    content = {'rooms': rooms, 'booked_rooms': booked_rooms}
    return render(request, 'room/room_home.html',content)

def create_room(request):
    form=room_form()
    if request.method == "POST":
        return _extracted_from_create_room_4(request)
    content={"form":form}
    return render(request, 'room/create_room.html',content)


# TODO Rename this here and in `create_room`
def _extracted_from_create_room_4(request):
    form=room_form(request.POST,request.FILES)
    form.user=request.user

    if form.is_valid():
        room=form.save(commit=False)
        room.user=request.user
        room.save()
        return redirect("home-room")
    return redirect("create-room")
def delete_room(request,pk):
    room=get_object_or_404(Room,pk=pk)
    if request.method == "POST":
        room.delete()
    # room.delete()
    return render(request,"room/delete.html")
from django.db import IntegrityError

def booking_room(request, pk):
    room = Room.objects.get(id=pk)
    gst = int(((room.price) * 18) / 100)
    

    if request.method == "POST":
        startdate = request.POST.get("startdate")
        enddate = request.POST.get("enddate")

        if startdate and enddate:
            start_datetime = datetime.strptime(startdate, '%Y-%m-%d')
            end_datetime = datetime.strptime(enddate, '%Y-%m-%d')
            duration = (end_datetime - start_datetime).days
            total = (room.price + gst) * duration

            try:
                book = room.booking_set.create(
                    user=request.user,
                    room=room,
                    start_date=start_datetime,
                    end_date=end_datetime,
                    total_price=total,
                    duration=duration 
                )
                receiver_mail=book.user.email
                send_mail_to_user_after_booking(book.user)
                return redirect("home-room")
            except IntegrityError as e:
                # Handle the IntegrityError, maybe by showing an error message to the user
                pass

    # If the request method is not POST or if there was an error in creating the booking, render the form
    content = {"room": room}
    return render(request, "room/booking_form.html", content)

    