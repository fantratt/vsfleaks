from vsfleakssite.models import *
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext as _

    
class ReportForm(forms.ModelForm):
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                             error_message = _("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),
                             required=False)
    class Meta:
        model = Report
        fields = (_('subject'), _('message'), _('file'), _('name'), _('email'))
    
