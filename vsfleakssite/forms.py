from vsfleakssite.models import *
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext as _


class UserForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(), label=_("email"))
    password = forms.CharField(widget=forms.PasswordInput(), label=_("password"))
    
    class Meta:
        model = User
        fields = ('email', 'password')
    
    def save(self, commit=False):
        instance = super(UserForm, self).save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance
    
class ReportForm(forms.ModelForm):
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                             error_message = _("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),
                             required=False)
    
    class Meta:
        model = Report
        fields = ('subject', 'message', 'file', 'name', 'email')
    
