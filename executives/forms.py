from django import forms
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

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'organization', 'start_date', 'end_date']

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


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
