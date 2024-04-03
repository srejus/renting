from django.shortcuts import render,redirect
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from renting.models import Listing
from accounts.models import Account


# Create your views here.
class IndexView(View):
    def get(self,request):
        msg = request.GET.get("msg")
        return render(request,'index.html',{'msg':msg})
    

@method_decorator(login_required,name='dispatch')
class ListingView(View):
    def get(self,request):
        items = Listing.objects.filter(listed_by__user=request.user).order_by('-id')
        return render(request,'my_listing.html',{'items':items})


@method_decorator(login_required,name='dispatch')
class AddListingView(View):
    def get(self,request):
        return render(request,'add_listing.html')
    
    def post(self,request):
        item_name = request.POST.get('item_name')
        rent_per_day = request.POST.get('rent_per_day')
        item_image = request.FILES.get('item_image')
        description = request.POST.get('desc')
        category = request.POST.get('categorySelect')
        location = request.POST.get("location")
        
        acc = Account.objects.get(user=request.user)

        Listing.objects.create(item_name=item_name,item_image=item_image,
                               listed_by=acc,rent_price_per_day=rent_per_day,
                               description=description,category=category,
                               is_available=True,location=location)
        
        return redirect("/listing")

        
