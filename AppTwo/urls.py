from django.contrib import admin
from django.urls import path
from AppTwo import views
from django.conf.urls import include

urlpatterns = [
path('',views.users,name = 'users'),
]
