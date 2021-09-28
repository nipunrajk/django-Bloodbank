from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='Bloodbank-home'),
 path('display/', views.display, name='Bloodbank-display')
]