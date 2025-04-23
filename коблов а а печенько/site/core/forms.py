from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CertificateOrder
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']

class CertificateOrderForm(forms.ModelForm):
    class Meta:
        model = CertificateOrder
        fields = ['purpose']