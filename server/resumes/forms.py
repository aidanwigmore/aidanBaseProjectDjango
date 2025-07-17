from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    extra_field = forms.CharField(required=False, label="Extra Info")

    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ex: Firstname Lastname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ex: name@mail.com'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ex: 123-456-7890'}),
        }