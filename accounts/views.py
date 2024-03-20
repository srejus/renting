from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

from project.utils import send_mail

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *

# Create your views here.

class LoginView(View):
    def get(self,request):
        err = request.GET.get("err")
        type_ = request.GET.get("type","user")
        if type_ == "user":
            title = "LOGIN TO YOUR ACCOUNT"
        elif type_ == 'admin':
            title = "ADMIN LOGIN"
        else:
            title = "LOGIN AS DELIVERY AGENT"
        return render(request,'login.html',{'err':err,"type":title})

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        type_ = request.GET.get("type","user")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            acc = Account.objects.get(user=user)
            if type_ == 'user' and acc.user_type != Account.USER:
                err = "Invalid user credentials!"
                return redirect(f"/accounts/login/?err={err}")
            if type_ == 'admin' and acc.user_type != Account.ADMIN:
                err = "Invalid user credentials!"
                return redirect(f"/accounts/login/?err={err}")
            if type_ == 'delivery' and acc.user_type != Account.DELIVERY_AGENT:
                err = "Invalid user credentials!"
                return redirect(f"/accounts/login/?err={err}")
            login(request, user)
            next = request.GET.get("next")
            if next:
                return redirect(next)
            
            if type_ == 'delivery':
                return redirect("/delivery/")
            
            if type_ == 'admin':
                return redirect("/adminuser/")
            return redirect("/")
        err = "Invalid credentails!"
        return redirect(f"/account/login/?err={err}")
    

class SignupView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'signup.html',{'err':err})
    
    def post(self,request):
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        pincode = request.POST.get("pincode")
        landmark = request.POST.get("landmark")
        user_type = request.POST.get("user_type","USER")

        if password1 != password2:
            err = "Password not matching!"
            return redirect(f"/accounts/signup?err={err}")

        user = User.objects.filter(username=username)
        if user.exists():
            err = "User with this username already exists"
            return redirect(f"/accounts/signup?err={err}")
        
        acc = Account.objects.filter(Q(email=email) | Q(phone=phone)).exists()
        if acc:
            err = "User with this phone or email already exists"
            return redirect(f"/accounts/signup?err={err}")
        
        user = User.objects.create_user(username=username,email=email,password=password1)
        acc = Account.objects.create(user=user,full_name=full_name,phone=phone,
                                     email=email,address1=address1,address2=address2,pincode=pincode,
                                     landmark=landmark,user_type=user_type)
        
         # sending email
        subject = "Welcome to Rentit!"
        to_email = email
        content = f"Hello {full_name},\nWelcome to Rentit. You can now place Rent request to various items listed in the webiste \n\n Thanks \nTeam RentIt"
        send_mail(to_email,subject,content)

        return redirect('/accounts/login')
    

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/")
    

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        return render(request,'profile.html',{'acc':acc})
    

@method_decorator(login_required,name='dispatch')
class EditProfileView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        return render(request,'edit_profile.html',{'acc':acc})
    
    def post(self,request):
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        pincode = request.POST.get("pincode")
        landmark = request.POST.get("landmark")

        acc = Account.objects.get(user=request.user)

        acc.full_name = full_name
        acc.phone = phone
        acc.email = email
        acc.address1 = address1
        acc.address2 = address2
        acc.pincode = pincode
        acc.landmark = landmark
        acc.save()
        return redirect("/accounts/profile")

    