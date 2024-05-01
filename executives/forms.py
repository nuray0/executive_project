from django import forms
from django.core.exceptions import ValidationError

from .models import Executive, WorkExperience, Certificate, PositionConsent, Education

class ExecutiveForm(forms.ModelForm):
    class Meta:
        model = Executive
        fields = ['first_name', 'last_name', 'country', 'resume', 'is_resident']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].label = 'Resume in PDF'

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company', 'start_date', 'end_date']

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date == end_date:
                raise ValidationError("Start date and end date must be different")
            if start_date > end_date:
                raise ValidationError("Start date must be earlier than end date")


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'organization', 'start_date', 'end_date']

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date == end_date:
                raise ValidationError("Start date and end date must be different")
            if start_date > end_date:
                raise ValidationError("Start date must be earlier than end date")
            

class PositionConsentForm(forms.ModelForm):
    class Meta:
        model = PositionConsent
        fields = ['issue_date', 'protocol_number']

        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'})
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['university', 'graduation_year', 'degree', 'specialization']
