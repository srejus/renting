from django.urls import path
from .views import *

urlpatterns = [
    path('',RentView.as_view()),
]