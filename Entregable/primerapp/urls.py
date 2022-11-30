from django.urls import path
from primerapp import views
from primerapp.views import *

urlpatterns = [
    path("familiar/", familiar),
    
]