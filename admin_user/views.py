from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import *
from accounts.models import Account
from renting.models import *

# Create your views here.
class AdminLoginView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'admin_login.html',{'err':err})

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if not user.superuser_status:
            err = "Invalid admin credentails!"
            return redirect(f"/adminuser/login/?err={err}") 
        if user is not None:
            login(request, user)
            next = request.GET.get("next")
            if next:
                return redirect(next)
            return redirect("/adminuser/")
        err = "Invalid credentails!"
        return redirect(f"/adminuser/login/?err={err}")
    

@method_decorator(login_required,name='dispatch')
class AdminHomeView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        return render(request,'admin_home.html',{'acc':acc})
    

@method_decorator(login_required,name='dispatch')
class AdminUsersView(View):
    def get(self,request):
        users = Account.objects.all()
        return render(request,'admin_users.html',{"users":users})
    

@method_decorator(login_required,name='dispatch')
class AdminRentsView(View):
    def get(self,request):
        rents = RentedItem.objects.all().order_by('-id')
        return render(request,'admin_rents.html',{'rents':rents})
    


@method_decorator(login_required,name='dispatch')
class AdminRentRejectView(View):
    def get(self,request,id):
        RentedItem.objects.filter(id=id).update(status='REJECTED')
        return redirect("/adminuser/rents")
    

@method_decorator(login_required,name='dispatch')
class AdminRentAcceptView(View):
    def get(self,request,id):
        RentedItem.objects.filter(id=id).update(status='ACCEPTED')
        return redirect("/adminuser/rents")
    