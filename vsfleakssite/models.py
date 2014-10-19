from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings 
from django.utils.translation import ugettext as _
# Create your models here.

class Report(models.Model):
    subject = models.CharField(_('subject'), max_length=225, blank=False)
    message = models.TextField( _('message'), blank=False)
    file = models.FileField(_('file'), null=True, blank=True, upload_to='uploads/%y%m%d%H%M/')
    name = models.CharField( _('name'), max_length=225, blank=True)
    phone = models.CharField( _('phone'), max_length=15, blank=True)
    email = models.EmailField(_('email'), blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject

