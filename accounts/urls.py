from django.urls import path
from .views import *

urlpatterns = [
    path('login/',LoginView.as_view()),
    path('signup',SignupView.as_view()),
    path('logout',LogoutView.as_view()),
    path('profile',ProfileView.as_view()),
    path('profile/edit',EditProfileView.as_view()),
]