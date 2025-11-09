from projects.views import *
from django.urls import path
from .views import*

urlpatterns = [
    path ('project/',project),
    path ('project_details/',project_details),
   
]