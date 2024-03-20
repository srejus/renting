from django.urls import path
from .views import *

urlpatterns = [
    path('',RentView.as_view()),
    path('<int:id>',ItemRentView.as_view()),

    path('my-orders',MyOrdersView.as_view()),
]