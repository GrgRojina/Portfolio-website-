from django.db import models


# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=50)
    titles =models.CharField(max_length=150)
    email =models.EmailField()
    phone_num =models.CharField(max_length=15, blank=True, null=True)
    address =models.CharField(max_length=200)
    age =models.IntegerField()
    google_map_link = models.URLField(blank=True, null=True)
    summery= models.TextField(blank=True, null=True)
    freelance =models.BooleanField(default =True)
    degree =models.CharField(max_length=200, blank =True, null=True)
    profile_image =models.ImageField(blank=True, null=True)
    cover_image =models.ImageField(blank=True, null=True)

class Socials(models.Model):
    name= models.CharField(max_length=50)
    icon=models.ImageField()
    url= models.URLField()
    

    def __str__(self):
        return self.name
    
class Statistics(models.Model):
    name= models.CharField(max_length=50)
    number=models.IntegerField()
    icon=models.ImageField()

    def __str__(self):
        return f'{self.name}=>{self.number}'
    

class Skills(models.Model):
    name =models.CharField(max_length=100)
    percentage =models.IntegerField(help_text="Skill learn in percentage")

    def __str__(self):
        return self.name

class Service(models.Model):
    icon = models.CharField(max_length=100)  # Store icon class name or path
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"Enquiry from {self.name} - {self.subject}"


