from django.urls import path
from .views import *

urlpatterns = [
    path('',AdminHomeView.as_view()),
    path('login/',AdminLoginView.as_view()),
    path('users',AdminUsersView.as_view()),
    path('rents',AdminRentsView.as_view()),
    path('rents/reject/<int:id>',AdminRentRejectView.as_view()),
    path('rents/accept/<int:id>',AdminRentAcceptView.as_view()),
]
