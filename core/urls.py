
from django.urls import path
#from .views import render_home
from core.views import *

urlpatterns = [
    path ('',render_home, name= 'home'),
    path ('About/',render_about),
    path ('Contact/',render_Contact),
    path('contact-list/',contact_list),
    path('contact-delete/<int:id>', contact_delete, name ="contact_delete"),
    #path ('Contact/',render_Contact2),
    #path ('portfolio-details/',render_portfolio)
    
    ]