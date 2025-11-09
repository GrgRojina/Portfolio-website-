from .views import experience, experience_details
from django.urls import path


urlpatterns = [
    path('experience/', experience),
    path('experience_details/', experience_details),
]
