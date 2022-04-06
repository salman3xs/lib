from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Book(models.Model):
    author = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    about = models.TextField()
    published_date = models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(('email'), unique=True) # changes email to unique and blank to false
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS