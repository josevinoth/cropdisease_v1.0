# main/forms.py
from django import forms
from .models import Registration,UserQuery

class UserQueryForm(forms.ModelForm):
    class Meta:
        model = UserQuery
        fields = ['name', 'email', 'query']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'mobile_number', 'user_type']