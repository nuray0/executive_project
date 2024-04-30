from django.contrib import admin

from .models import Executive, WorkExperience, Certificate, PositionConsent, Education

admin.site.register(Executive)
admin.site.register(WorkExperience)
admin.site.register(Certificate)
admin.site.register(PositionConsent)
admin.site.register(Education)
