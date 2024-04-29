from django.shortcuts import render, HttpResponse, redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
import json
# states
def home(request):
    data = state.objects.all()
    print("->" ,data.values())
    context = {
        'data' : data
    }
    print("==> context is", context)
    return render(request , "index.html" , context)

# destinations
def index(request):    
    data = Image.objects.all()
    print("->" ,data.values())
    context = {
        'data' : data
    }
    return render(request,"display.html", context)

# hotels
def hotels(request):
    data = Hotels.objects.all()
    print("->", data.values())
    context = {
        'data' : data
    }
    return render(request , "hotels.html" , context)

def checkout(request):
    data = Hotels.objects.all()
    print("->", data.values())
    context = {
        'data' : data
    }
    return render(request , "checkout.html" , context)

# def booking(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone_number = request.POST.get('phone_number')
#         number_of_peoples = request.POST.get('number_of_peoples')
#         number_of_rooms = request.POST.get('number_of_rooms')
#         check_in_date = request.POST.get('check_in_date')
#         chekout_out_date = request.POST.get('chekout_out_date')
#         print("->" ,name , phone_number , number_of_peoples , number_of_rooms , check_in_date , chekout_out_date)
#         booking = Booking.objects.create(name = name , phone_number = phone_number , number_of_peoples = number_of_peoples , number_of_rooms = number_of_rooms , check_in_date = check_in_date , chekout_out_date = chekout_out_date)
#         booking.save()
#         messages.success(request , "Your Booking has been confirmed")
#         return redirect('/hotels')
#     else:
#         return HttpResponse("404 Not Found")

class DoBookingAPI(APIView):
    def post(self, request, *args, **kwargs):

        response = {}
        data = request.data["json_string"]
        data = json.loads(data)
        print("==> data", type(data))
        name = data["name"]
        phone_number = data["phone_number"]
        number_of_peoples = data["number_of_peoples"]
        number_of_rooms = data["number_of_rooms"]
        check_in_date = data["check_in_date"]
        chekout_out_date = data["chekout_out_date"]
        amount = data["amount"]
        print(name, phone_number, number_of_peoples , number_of_rooms, check_in_date , chekout_out_date, amount)
        obj = Booking.objects.create(name = name, phone_number = phone_number , number_of_peoples = number_of_peoples , number_of_rooms = number_of_rooms , check_in_date= check_in_date , chekout_out_date = chekout_out_date, amount = amount)
        obj.save()
        return Response(data = response , status = status.HTTP_201_CREATED)

DoBooking = DoBookingAPI.as_view()
    

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        # Check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('/')
        
        #  create the user
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('/')
        if(not email):
            myuser = User.objects.create_user(username = username ,password= pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
        else:
            myuser = User.objects.create_user(username = username ,email = email,password= pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
        messages.success(request , "Your SafarNaama account has been successfully created.")
        return redirect('/')

    else:
        return HttpResponse("404 Not Found")

def handleLogin(request):
    if request.method == 'POST':
        print("==> yes in login")
        # Get the post parameters
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        user = authenticate(username = loginusername, password = loginpassword)
        if user is not None:
            login(request , user)
            messages.success(request , "Successfully logged in")
        else:
            messages.error(request , "Invalid credentials please try again")
        return redirect('/')
    return HttpResponse("handle login")

def handleLogout(request):
   
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

    return HttpResponse("handle logout")


