from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *

# Create your views here.
class RentView(View):
    def get(self,request):
        category = request.GET.get("item")
        location = request.GET.get("location")
        if location:
            items = Listing.objects.filter(item_name__icontains=category,is_available=True,location=location).order_by('-id')
        else:
            items = Listing.objects.filter(item_name__icontains=category,is_available=True).order_by('-id')
        return render(request,'listing.html',{'items':items})
    

@method_decorator(login_required,name='dispatch')
class ItemRentView(View):
    def get(self,request,id=None):
        acc = Account.objects.get(user=request.user)
        item = Listing.objects.get(id=id)
        return render(request,'rent_form.html',{'acc':acc,'item':item})

    def post(self,request,id=None):
        full_name = request.POST.get("full_name")
        address1 = request.POST.get("address1")
        phone = request.POST.get("phone")
        pincode = request.POST.get("pincode")
        landmark = request.POST.get("landmark")
        no_of_days = request.POST.get("no_of_days")
        qnty = request.POST.get("qnty")

        acc = Account.objects.get(user=request.user)
        item = Listing.objects.get(id=id)

        RentedItem.objects.create(
            user=acc,item=item,full_name=full_name,phone=phone,pincode=pincode,landmark=landmark,address=address1,
            no_of_days=no_of_days,qnty=qnty
        )

        return render(request,'thanks.html')
        # return redirect(f"/?msg={msg}")


@method_decorator(login_required,name='dispatch')
class MyOrdersView(View):
    def get(self,request,id=None):
        items = RentedItem.objects.filter(user__user=request.user).order_by('-id')
        return render(request,'my_orders.html',{'items':items})
    