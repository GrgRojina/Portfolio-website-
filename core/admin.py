from django.contrib import admin
from .models import Bio, Socials, Statistics,Skills,Service,Testimonial,Enquiry

# Register your models here.
admin.site.register(Bio)
admin.site.register(Socials)
admin.site.register(Statistics)
admin.site.register(Skills)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Enquiry)