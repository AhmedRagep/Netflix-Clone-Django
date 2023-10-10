from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('profiles', views.ProfileList.as_view(), name='profile_list'),
]
