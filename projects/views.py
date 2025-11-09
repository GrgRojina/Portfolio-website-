from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def project(request):
    return HttpResponse("Project sucessfully install")

def project_details(request):
    #return HttpResponse("Here is the project details")
    return render(request, 'project-details.html')