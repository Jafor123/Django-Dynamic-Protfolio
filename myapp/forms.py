from django import forms
from myapp.models import Contactus
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields="__all__"