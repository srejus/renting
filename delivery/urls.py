from django.urls import path
from .views import *

urlpatterns = [
    path('',DeliveryHomeView.as_view()),
    path('orders',DeliveryOrdersView.as_view()),
    path('orders/pickup/<int:id>',DeliveryOrdersPUView.as_view()),
    path('orders/delivered/<int:id>',DeliveryOrdersDeliView.as_view()),
    path('earning',DeliveryEarningView.as_view()),
]