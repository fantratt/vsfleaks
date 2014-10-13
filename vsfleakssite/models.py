from django.db import models
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Report(models.Model):
    subject = models.CharField(max_length=225, blank=False)
    message = models.TextField(blank=False)
    file = models.FileField(null=True, blank=True, upload_to='documents/%Y/%m/%d')
    name = models.CharField(max_length=225, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject
    
class Post(models.Model):
    report = models.ForeignKey('Report', null=True, blank=True)
    title = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(unique=True, max_length = 255)
    description = models.CharField(max_length = 255)
    content = models.TextField(blank=False)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('vsfleaks:post', args=[self.slug]) 
        
