from django import forms
from django.forms import ModelForm
from django.forms.widgets import EmailInput, Textarea, TextInput

from .models import Contact, Email

CHOICES = [("For Program", "For Program"), ("For Appointment", "For Appointment")]


class ContactForm(forms.ModelForm):
    choices = forms.CharField(
        widget=forms.RadioSelect(choices=CHOICES, attrs={"class": "form-check-input"})
    )

    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Name",
                    "autocomplete": "off",
                }
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "phone"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control ",
                    "placeholder": "Email",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control ",
                    "placeholder": "Type Your Message",
                }
            ),
        }


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control ",
                    "placeholder": "Enter your email address",
                }
            ),
        }
