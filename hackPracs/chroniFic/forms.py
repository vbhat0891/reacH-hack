from django import forms
from .models import Patient


class ContactForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('pFirstName', 'pLastName', 'pContactNumber')