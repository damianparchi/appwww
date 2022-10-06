from django.urls import path
from . import views

urlpatterns = [
    path('sayhi/', views.say_hi),
    path('sayhitwo/', views.say_secondtime)
]