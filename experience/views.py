from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def experience(request):
    template = "experience.html"
    return render(request, template)

def experience_details(request):
    template = "details.html"
    return render(request, template)
