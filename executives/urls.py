from django.urls import path
from . import views

app_name = 'executives'
urlpatterns = [
    path('add/', views.executive_add, name='add'),
    path('<int:pk>/edit/', views.executive_edit, name='edit'),
    path('<int:pk>/delete/', views.executive_delete, name='delete'),
    path('<int:pk>/', views.executive_detail, name='detail'),

    path('<int:pk>/work-experience/add', views.work_experience_add, name = 'work_experience_add'),
    path('<int:pk>/work-experience/', views.work_experience_list, name = 'work_experience_list'),
    path('<int:pk>/work-experience/<int:work_experience_pk>/edit/', views.work_experience_edit, name = 'work_experience_edit'),
    path('<int:pk>/work-experience/<int:work_experience_pk>/delete/', views.work_experience_delete, name = 'work_experience_delete'),

    path('<int:pk>/certificate/add/', views.certificate_add, name = 'certificate_add'),
    path('<int:pk>/certificate/<int:certificate_pk>/edit/', views.certificate_edit, name = 'certificate_edit'),
    path('<int:pk>/certificate/<int:certificate_pk>/delete/', views.certificate_delete, name = 'certificate_delete'),
    path('<int:pk>/certificate/', views.certificate_list, name = 'certificate_list'),

    path('<int:pk>/position-consent/add/', views.position_consent_add, name = 'position_consent_add'),
    path('<int:pk>/position_consent/<int:position_consent_pk>/edit/', views.position_consent_edit, name = 'position_consent_edit'),
    path('<int:pk>/position_consent/<int:position_consent_pk>/delete/', views.position_consent_delete, name = 'position_consent_delete'),
    path('<int:pk>/position-consent/', views.position_consent_list, name = 'position_consent_list'),

    path('<int:pk>/education/add/', views.education_add, name = 'education_add'),
    path('<int:pk>/education/<int:education_pk>/edit/', views.education_edit, name = 'education_edit'),
    path('<int:pk>/education/<int:education_pk>/delete/', views.education_delete, name = 'education_delete'),
    path('<int:pk>/education/', views.education_list, name = 'education_list'),

    path('resume/<int:pk>/', views.serve_resume, name='serve_resume'),
]