from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from .forms import restaurant_form
from django.contrib.auth.models import User
from base.models import restaurants,hotel,dish,orders
from django.contrib.auth import login ,authenticate,logout
from  django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import aggregates
import random
from accounts.models import UserProfile

# Create your views here.

@login_required(login_url="login-page ")
def create_restaurant(request):
    hotel_obj=hotel.objects.get(id=2)
    # form=restaurant_form()
    if request.method == "POST":
        restaurantName=request.POST.get("restaurantName")
        locations=request.POST.get("locations")
        image=request.FILES.get("image")
        try:
            restaurant_obj=restaurants.objects.create(
                restaurantName=restaurantName,
                locations=locations,
                image=image,
            hotel=hotel_obj,
            user=request.user
            )
        except Exception as e:
            messages.error(request,e)
        
        restaurant_obj.save()
        return redirect("home")
    # content={"form":form}
    return render(request,"base/restaurantform.html")
@login_required(login_url="login-page")
def update_restaurant(request,pk):
    restaurant_obj=restaurants.objects.get(id=pk)
    if request.method == "POST":
        restaurantName=request.POST.get("restaurantName")
        locations=request.POST.get("locations")
        image=request.FILES.get("image")
        restaurant_obj.restaurantName = restaurantName
        restaurant_obj.locations = locations
        if restaurant_obj.image:
            restaurant_obj.image = image
        restaurant_obj.save()
        return redirect("home")
    content={"restaurant":restaurant_obj}
    return render(request,"base/restaurantform.html",content)
@login_required(login_url="login-page")
def delete_restaurant(request,pk):
    restaurant_obj=restaurants.objects.get(id=pk)
    if request.method == "POST":
        restaurant_obj.delete()
        return redirect("home")
    content={"obj":restaurant_obj}
    return render(request,"base/delete_restaurant.html",content)
def restaurant_data(request,pk):
    restaurant=restaurants.objects.get(id=pk)
    q= request.GET.get("q")
    dishes=restaurant.dish_set.all()
    create_dish(request,restaurant.id)
    if q is not None :
        try:
            num_q=float(q)
            dishes=dishes.filter(
                                Q(dishName__icontains=q) |
                                Q(description__icontains=q) |
                                Q(price__lte=q)    
                                )
        except Exception:
            dishes=dishes.filter(
                                Q(dishName__icontains=q) |
                                Q(description__icontains=q)    
                                )
    if under_value := request.GET.get('count') is not None:
        dishes=restaurant.dish_set.all()
        dishes=dishes.filter(price__lt=under_value)   
    content={"restaurant":restaurant,"dishes":dishes}
    return render(request,"base/restaurant_data.html",content)
@login_required(login_url="login-page")
def delete_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    restaurant=dish_obj.restaurants
    dish_obj.delete()
    return redirect("restaurant-data",pk=restaurant.id)
@login_required(login_url="login-page")
def update_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    dishname=request.POST.get("dishname")
    dish_description=request.POST.get("description")
    dishimage= request.FILES.get("dishImage")  
    price= request.POST.get("price")
    restaurant=dish_obj.restaurants
    if request.method == "POST":
        if dishname :
            dish_obj.dishName=dishname
            dish_obj.description=dish_description
            if dishimage:
                dish_obj.dishImage = dishimage
            dish_obj.price=price    
        dish_obj.save()
        return redirect("restaurant-data",pk=restaurant.id)
    content={"restaurant":restaurant,"dish_obj":dish_obj}
    return render(request,"base/update_dish.html",content)

# def blank(request):
#     # form=user_form()
#     context={"form":form}
#     return render(request,"blank_form.html",context)

def create_dish(request,pk):
    restaurant=restaurants.objects.get(id=pk)
    if request.method == "POST":
        try:
            
            create_dishes=dish.objects.create(
                    dishName=request.POST.get("dishname"),
                    description=request.POST.get("description"),
                    dishImage=request.FILES.get("dishImage"),
                    user=request.user,
                    hotel=restaurant.hotel,
                    restaurants=restaurant,
                    price=request.POST.get("price"),
                    ) 
        except Exception as e:
            messages.error(request,e)
        return redirect("restaurant-data",pk=restaurant.id)
    content={"restaurant":restaurant}    
    return render(request,'base/dishform.html',content)

def order_dish(request,pk):
    dishe=dish.objects.get(id=pk)
    delavery_charge=int(dishe.price * 0.10)
    location=request.POST.get("location")
    if request.method == "POST":
        try:
            order=orders.objects.create(
                delivery_charges=delavery_charge,
                total_charges=(dishe.price+delavery_charge)*1.18,
                location=location,
                restaurants=dishe.restaurants,
                dish=dishe,
                user=request.user
            )
            order.save()
            return redirect("restaurant-data",pk=dishe.restaurants.id )
        except Exception as e:
            print(e)
    content={"dish":dishe,"delivery":delavery_charge}
    return render(request,"base/order_dish.html",content)
        
    
    