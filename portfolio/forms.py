from django.forms import ModelForm
from .models import Contact
from django import forms
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "phone_number", "email", "message"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")
        return name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only numbers.")
        if len(phone_number) < 9:
            raise forms.ValidationError("Phone number must be at least 9 characters.")
        return phone_number

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError("Please enter a message.")
        return message
