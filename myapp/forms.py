from django import forms
from .models import Contact
from .models import InquiryForm
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "comment"]

class InquiryForm(forms.ModelForm):
    class Meta:
        model = InquiryForm
        fields = ["first_name","last_name", "email", "number", "comment"]
