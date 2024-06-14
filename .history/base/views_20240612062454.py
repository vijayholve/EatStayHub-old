from django.shortcuts import render,redirect,HttpResponse
from .form import restaurant_form
from django.contrib.auth.models import User
from .models import restaurants,hotel,dish,orders
from django.contrib.auth import login ,authenticate,logout
from  django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import aggregates
import random
from accounts.models import UserProfile
from .seed import register_user_to_send_mail,email_for_otp_verification
from .tasks import send_mail_task
def home(request):
    q=request.GET.get("q") 
    users=User.objects.all()
    restaurant=restaurants.objects.all()
    if q :   
        restaurant=restaurants.objects.filter(Q(restaurantName__icontains=q) |
                                              Q(locations__icontains=q))
    
    # dishes=restaurants.dishes.all()
    content={"users":users,"restaurants":restaurant,"dish":dish}
    return render(request,"base/home.html",content)

def login_page(request):
    page="login"
    username=request.POST.get("username")
    password=request.POST.get("password")
    if request.method == "POST":
        try:
            user=User.objects.get(username=username)
        except Exception as e:
            messages.error(request,f"error is {e}")
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else :
            messages.error(request,"incorect username and password ")
    context={"page":page}
    return render(request,"base/login_page.html",context)
def register(request):
    page="resister"
    if request.method =="POST":
        return _extracted_from_register_4(request)
    context={"page":page}
    return render(request,"base/login_page.html",context)
# TODO Rename this here and in `register`
def _extracted_from_register_4(request):
    fullname=request.POST.get("fullname")
    email=request.POST.get("email")
    username=request.POST.get("username")
    password=request.POST.get("password")
    confirm_password=request.POST.get("confirm-password")
    print(fullname," ",email," ",username," ",password," ",confirm_password)
    if password != confirm_password :
        messages.error(request,"Password Does Not Matching")
        return redirect("register")
    if username is None or len(username) <  3 :
        messages.error(request,"please enter username")
        return redirect("register")
    if fullname is None or len(fullname) <= 5:
        messages.error(request,"please enter fullname")
        return redirect("register")
    if email is None or len(email) <= 5:
        messages.error(request,"please enter email")
        return redirect("register")
    picture=request.FILES.get("profilePicture")
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        profile = UserProfile.objects.create(user=user, profilePicture=picture, dateOfBirth=None)
        profile.save()

        login(request, user)
        send_mail_task.delay(email, fullname)
        return redirect("home")
    except Exception as e:
        print(e)
        messages.error(request, "There was an error creating your profile.")
        context = {"page": "register"}
        return render(request, "base/login_page.html", context)


# TODO Rename this here and in `register`

    
@login_required(login_url="login-page")
def logout_page(request):
    logout(request)
    return redirect("login-page")

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
    return render(request,"restaurant/restaurantform.html")

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
    return render(request,"restaurant/restaurantform.html",content)
@login_required(login_url="login-page")
def delete_restaurant(request,pk):
    restaurant_obj=restaurants.objects.get(id=pk)
    if request.method == "POST":
        restaurant_obj.delete()
        return redirect("home")
    content={"obj":restaurant_obj}
    return render(request,"restaurant/delete_restaurant.html",content)