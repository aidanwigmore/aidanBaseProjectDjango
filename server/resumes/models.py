from django.db import models
from django import forms
from django.forms import inlineformset_factory

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    
class ResumeURL(models.Model):
    resume = models.ForeignKey(Resume, related_name='urls', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return f"{self.label} - {self.url}"

ACCREDITATION_CHOICES = [
    (0, 'None'),
    (1, 'Certificate'),
    (2, 'Diploma'),
    (3, 'Advanced Diploma'),
    (4, 'Associate Degree'),
    (5, 'Master Degree'),
    (6, 'Doctorate Degree'),
]

INSTITUTION_TYPE_CHOICES = [
    (0, 'None'),
    (1, 'College'),
    (2, 'University'),
]

class ResumeEducation(models.Model):
    resume = models.ForeignKey(Resume, related_name='education', on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100)
    program_name = models.CharField(max_length=100, blank=True)
    
    institution_type = models.IntegerField(choices=INSTITUTION_TYPE_CHOICES, default=0)
    accreditation = models.IntegerField(choices=ACCREDITATION_CHOICES, default=0)
    
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.institution_name} - {self.accredation}"

class ResumeSkill(models.Model):
    resume = models.ForeignKey(Resume, related_name='skills', on_delete=models.CASCADE)
    skill_label = models.CharField(max_length=100)
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.skill_label} - {self.skill_name}%"

class ResumeExperience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experience', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class ResumeProject(models.Model):
    resume = models.ForeignKey(Resume, related_name='projects', on_delete=models.CASCADE)
    project_nickname = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_url = models.URLField(blank=True)
    project_description = models.TextField(blank=True)

    def __str__(self):
        return self.project_name

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone']

    ResumeURLFormSet = inlineformset_factory(
        Resume, ResumeURL,
        fields=['label', 'url'],
        extra=1,
        can_delete=True
    )