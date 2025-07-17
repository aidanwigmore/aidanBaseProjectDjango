from django.db import models

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

class ResumeEducation(models.Model):
    resume = models.ForeignKey(Resume, related_name='education', on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100)
    institution_type = models.BooleanField(default=False)
    program_name = models.CharField(max_length=100, blank=True)
    
    accreditation = models.IntegerField(default=0)
    # none - 0
    # certificate - 1
    # diploma - 2
    # advanced diploma - 3
    # associate degree - 4
    # master degree - 5
    # doctorate degree - 6
    
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.institution_name} - {self.degree}"

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