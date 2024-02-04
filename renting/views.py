from django.shortcuts import render,redirect
from django.views import View

from .models import Listing

# Create your views here.
class RentView(View):
    def get(self,request):
        category = request.GET.get("item")
        location = request.GET.get("location")
        items = Listing.objects.filter(is_available=True,location=location).order_by('-id')
        return render(request,'listing.html',{'items':items})
