from django.urls import path
from blogs.views import *

urlpatterns = [
     path ('blog/',blog),
     path ('blog_details/',blog_details),

]