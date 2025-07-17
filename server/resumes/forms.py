from django import forms
from .models import Resume, ResumeURL
from django.forms import inlineformset_factory

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

ResumeURLFormSet = inlineformset_factory(
    Resume, ResumeURL,
    fields=['label', 'url'],
    labels = {
        'label': 'Website Name',
        'url': 'URL',
    },
    widgets = {
        'label': forms.TextInput(attrs={'placeholder': 'Ex: Website Name'}),
        'url': forms.TextInput(attrs={'placeholder': 'Ex: https://example.com'}),
    },
    extra=1,
    can_delete=True
)

