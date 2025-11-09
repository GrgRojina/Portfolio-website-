from django.db import models

# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length=150)
    category =models.CharField(max_length  =200)
    start_year =models.IntegerField()
    end_year =models.IntegerField(blank=True, null=True)
    description = models.TextField()
    organization = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    

class Project(models.Model):
    category =models.CharField(max_length=200)
    title = models.CharField(max_length=150)
    link = models.URLField(blank=True, null=True)
    client = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    summary = models.TextField()

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def str(self):
        return f"Image for {self.project.title}"

