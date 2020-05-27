from django.contrib import admin
from django.urls import path
from holachatapp import views

urlpatterns = [
    path('', views.index, name="index"),
]
