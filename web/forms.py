from django import forms
from django.forms import ModelForm
from django.forms import DateInput 
from django.forms.widgets import EmailInput, Textarea, TextInput

from .models import Contact, Email,PositionsToken

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



class YearSelectWidget(forms.Select):
    def __init__(self, attrs=None, choices=(), years_from=1990, years_to=2100):
        years = range(years_from, years_to + 1)
        choices = [(year, year) for year in years]
        super().__init__(attrs, choices)

class YearSelectFormField(forms.DateField):
    widget = YearSelectWidget

class PositionsTokenAdminForm(forms.ModelForm):
    class Meta:
        model = PositionsToken
        fields = '__all__'
        widgets = {
            'toyear': YearSelectWidget, 
            'fromdate': DateInput(attrs={'type': 'date'}),
        }