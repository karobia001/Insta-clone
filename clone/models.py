from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(max_length=10, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to = 'photos/',blank=True)
