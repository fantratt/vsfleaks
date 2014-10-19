from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings 
# Create your models here.

class Report(models.Model):
    subject = models.CharField(max_length=225, blank=False)
    message = models.TextField(blank=False)
    file = models.FileField(null=True, blank=True, upload_to='uploads/%Y/%m/%d')
    name = models.CharField(max_length=225, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject

