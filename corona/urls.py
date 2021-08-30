
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('covid/', views.index, name="covid"),
    path('about/', views.about, name="about"),
    

]
