from django import forms
from .models import Enquiry


# class Enquiry(forms.form):
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=200)
#     message = forms.CharField(widget=forms.Textarea(attrs={'rows':8,'cols':40}))

class UserEnquiryModelForm(forms.ModelForm):
    class Meta:
        model =Enquiry
        fields =['name','email','subject','message']