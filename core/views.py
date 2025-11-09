from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Bio,Statistics,Enquiry, Skills
from projects.models import Resume
from .models import Enquiry
from django.contrib import messages
from .forms import UserEnquiryModelForm

#from .forms import 

def render_home(request):
    if request.method=='POST':
        form=UserEnquiryModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thankyou for submitting ")
            return redirect('home')

    bio=Bio.objects.first()
    stat= Statistics.objects.all()
    skills = Skills.objects.all()
    resume = Resume.objects.all()
    enquiry_form =UserEnquiryModelForm()

    print("=============")
    print(bio)
    name = bio.name
    titles =bio.titles
    email =bio.email
    template = "index.html"
    context = {
         "bio": bio,
        "name": name,
        "title": titles,
        "email": email,
        "enquiry_form": enquiry_form,
        "stat": stat,
        "skills": skills,
        "resume": resume
    }
    return render(request,template,context)

def render_about(request):
    template = "about.html"
    return render(request, template)

def render_Contact(request):
    if request.method=="POST":
    #print(request)
        input_name=request.POST['name']
        input_email=request.POST['email']
        input_subject=request.POST['subject']
        input_message=request.POST['message']
        Enquiry.objects.create(
            name=input_name,
            email=input_email,
            subject=input_subject,
            message=input_message
        )
    #print(name,email,subject,)
    template = "contact.html"
    return render(request, template)


def contact_list (request):
    if request.user.is_superuser:
        contact_lists =Enquiry.objects.all()
        
        #print(contact_list)
        context ={
         'contact_list': contact_lists
        }
        return render(request,'contact/list.html', context)
    else:
        messages.error(request, 'You are not authorized')
        return redirect('home')

def contact_delete (request, id):
    if request.method =="POST":
        enquiryform= Enquiry.objects.get(id=id)
        enquiryform.delete()
        return redirect('contact_list')

    return render(request, 'contact/delete.html')


#def render_Contact2(request):
    if request.method=="POST":
    #print(request)
        print(request.POST)
        form = EnquiryForm(request)
        i#f form.is_valid():

    #context ={
         #'enquiry_form': EnquiryForm()

    # }
    #template = "contact.html"
    #return render(request, template)



#def render_portfolio(request):
    #template = "portfolio-details.html"
    #return render(request, template)

#def project_details(request):
    #template = "portfolio-details.html"
    #return render(request, template)