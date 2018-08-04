#from .views import *
from django.urls import path

from . import views

urlpatterns = [
    #path('', index, name='index'), Written by Luek (Correct and works)
    path('', views.index),
    path('<unit>/', views.page)
]
