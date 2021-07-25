from django import forms
from django.forms import ModelForm, TextInput, EmailInput

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 800px;',
                'placeholder': 'Email'
            }),
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 800px;',
                'placeholder': 'First and Last Name'
            }),
            'subject': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 800px;',
                'placeholder': 'Subject'
            }),
            'message': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 800px; padding-bottom: 15px',
                'placeholder': 'Leave Your Message Here'
            })
        }
