from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view()),
    path('listing',ListingView.as_view()),
    path('add-listing',AddListingView.as_view()),
]