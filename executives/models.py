from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.db import models

def validate_pdf_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    valid_extensions = ['.pdf']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Only PDF files are allowed.')

class Executive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = CountryField()
    resume = models.FileField(upload_to='resumes/', validators=[validate_pdf_extension])
    is_resident = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class WorkExperience(models.Model):
    executive = models.ForeignKey(Executive, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.company}, {self.start_date} - {self.end_date}"
    
class Certificate(models.Model):
    executive = models.ForeignKey(Executive, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Certificate {self.name}, {self.executive.first_name} {self.executive.last_name}"
    
class PositionConsent(models.Model):
    executive = models.ForeignKey(Executive, on_delete=models.CASCADE)
    issue_date = models.DateField()
    protocol_number = models.CharField(max_length=100)

    def __str__(self):
        return f"Consent for {self.executive.first_name} {self.executive.last_name}"
    
class Education(models.Model):
    executive = models.ForeignKey(Executive, on_delete=models.CASCADE)
    university = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Educational background of {self.executive.first_name} {self.executive.last_name}"
    
