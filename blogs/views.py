from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def blog(request):
    return HttpResponse("This is blog")

def blog_details(request):
    return HttpResponse("Here,is the blog details")
