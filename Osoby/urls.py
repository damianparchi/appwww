from django.urls import path
from . import views

urlpatterns = [
    path('', views.osoba_list),
    path('<int:pk>/', views.osoba_detail),
    path('post', views.osoba_post),
]