from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.models import Account
from renting.models import *
from .models import Earning

# Create your views here.
@method_decorator(login_required,name='dispatch')
class DeliveryHomeView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        if acc.user_type != Account.DELIVERY_AGENT:
            msg = "You don't have access to this page!"
            return redirect(f"/?msg={msg}")
        
        return render(request,'dp_home.html',{"acc":acc})
    

@method_decorator(login_required,name='dispatch')
class DeliveryOrdersView(View):
    def get(self,request):
        items = RentedItem.objects.filter(status__in=[RentedItem.ACCEPTED,RentedItem.PICKED_UP]).order_by('-id')
        return render(request,'dp_orders.html',{'items':items})
    

@method_decorator(login_required,name='dispatch')
class DeliveryEarningView(View):
    def get(self,request):
        earnings = Earning.objects.filter(user__user=request.user).order_by('-id')
        return render(request,'dp_earning.html',{'earnings':earnings})


@method_decorator(login_required,name='dispatch')
class DeliveryOrdersPUView(View):
    def get(self,request,id=None):
        RentedItem.objects.filter(id=id).update(status=RentedItem.PICKED_UP)
        
        return redirect("/delivery/orders")
    

@method_decorator(login_required,name='dispatch')
class DeliveryOrdersDeliView(View):
    def get(self,request,id=None):
        RentedItem.objects.filter(id=id).update(status=RentedItem.DELIVERED)
        item = RentedItem.objects.get(id=id)
        acc = Account.objects.get(user=request.user)
        Earning.objects.get_or_create(user=acc,item=item)
        return redirect("/delivery/orders")
    
