from django import forms
from .models import Resume, ResumeURL, ResumeEducation
from django.forms import inlineformset_factory
import os

def get_institution_choices():
    base_dir = os.path.dirname(__file__)
    colleges_path = os.path.join(base_dir, 'CADcolleges.txt')
    universities_path = os.path.join(base_dir, 'CADuniversities.txt')
    choices = set()
    for path in [colleges_path, universities_path]:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    name = line.strip()
                    if name:
                        choices.add((name, name))
    return sorted(list(choices), key=lambda x: x[1])

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

class ResumeEducationForm(forms.ModelForm):
    institution_name = forms.ChoiceField(
        choices=get_institution_choices(),
        widget=forms.Select(attrs={'placeholder': 'Ex: University Name'})
    )

    class Meta:
        model = ResumeEducation
        fields = ['institution_name', 'institution_type', 'program_name', 'accreditation', 'start_date', 'end_date']
        labels = {
            'institution_type': 'Institution Type',
            'institution_name': 'Institution Name',
            'program_name': 'Program Name',
            'accreditation': 'Accreditation',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }
        widgets = {
            'institution_type': forms.Select(attrs={'placeholder': 'Ex: Institution Type'}),
            'institution_name': forms.Select(attrs={'placeholder': 'Ex: Institution Name'}),
            'program_name': forms.TextInput(attrs={'placeholder': 'Ex: Program Name'}),
            'accreditation': forms.Select(attrs={'placeholder': 'Ex: Accreditation'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
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

ResumeEducationFormSet = inlineformset_factory(
    Resume,
    ResumeEducation,
    form=ResumeEducationForm,
    extra=1,
    can_delete=True
)