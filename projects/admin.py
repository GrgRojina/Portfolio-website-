from django.contrib import admin
from .models import Resume,Project, ProjectImage
# Register your models here.
admin.site.register(Resume)
admin.site.register(Project)
admin.site.register(ProjectImage)