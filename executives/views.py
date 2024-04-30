from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

import os

from .forms import ExecutiveForm, WorkExperienceForm, CertificateForm, PositionConsentForm, EducationForm
from .models import Executive, WorkExperience, Certificate, PositionConsent, Education


def serve_resume(request, pk):
    executive = Executive.objects.get(pk=pk)
    resume_path = executive.resume.path

    if os.path.exists(resume_path):
        print('Resume file exists')

    try:
        return FileResponse(open(resume_path, 'rb'), content_type='application/pdf')
    except Exception as e:
        print(f"Error serving resume: {e}")
        return HttpResponseServerError("An error occurred while serving the resume file.")
    

@login_required
def executive_add(request):
    if request.method == 'POST':
        form = ExecutiveForm(request.POST,request.FILES)
        print('form:', form)
        if form.is_valid():
            executive = form.save(commit=False)

            print('request user:', request.user)
            executive.user = request.user
            executive.save()

            messages.success(request, 'Executive added successfully')
            return redirect('dashboard:index')

        print('request is not valid')
    else:
        form = ExecutiveForm()
    return render(request, 'executives/executive_add.html', {'form': form})


@login_required
def executive_detail(request, pk):
    executive = get_object_or_404(Executive, user = request.user, pk=pk)
    return render(request, 'executives/executive_detail.html', {'executive': executive})


@login_required
def executive_edit(request, pk):
    executive = get_object_or_404(Executive, user=request.user, pk=pk)
    if request.method == "POST":
        form = ExecutiveForm(request.POST, request.FILES, instance=executive)
        if form.is_valid():
            # Check if a new file is uploaded
            if 'resume' in request.FILES:
                # Remove the existing file if it exists
                if executive.resume:
                    if os.path.exists(executive.resume.path):
                        os.remove(executive.resume.path)
            form.save()

            messages.success(request, 'Changes were saved')
            return redirect('dashboard:index')
    else:
        form = ExecutiveForm(instance=executive)
    return render(request, 'executives/executive_edit.html', {'form': form})


@login_required
def executive_delete(request, pk):
    executive = get_object_or_404(Executive, user=request.user, pk=pk)
    
    if request.method == 'POST':
        # If the user confirmed the deletion
        executive.delete()
        messages.success(request, 'The executive was deleted')
        return redirect('dashboard:index')

    return render(request, 'executives/executive_delete_confirm.html', {'executive': executive})


@login_required
def work_experience_add(request, pk):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        print('form:', form)
        if form.is_valid():
            work_experience = form.save(commit=False)
            executive = Executive.objects.get(pk=pk)
            work_experience.executive = executive
            work_experience.save()

            messages.success(request, 'Work experience added successfully')
            return redirect('executives:work_experience_list', pk=pk)

        print('request is not valid')
    else:
        form = WorkExperienceForm()
    return render(request, 'executives/work_experience_add.html', {'form': form})


@login_required
def work_experience_edit(request, pk, work_experience_pk):
    work_experience = get_object_or_404(WorkExperience, pk=work_experience_pk)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect('executives:work_experience_list', pk=pk)
    else:
        form = WorkExperienceForm(instance=work_experience)
    return render(request, 'executives/work_experience_edit.html', {'form': form})


@login_required
def work_experience_delete(request, pk, work_experience_pk):
    work_experience = get_object_or_404(WorkExperience, pk=work_experience_pk)

    if work_experience.executive.pk != pk:
        return render(request, 'core/404.html')

    work_experience.delete()
    return redirect('executives:work_experience_list', pk=pk)


@login_required
def work_experience_list(request, pk):
    executive = Executive.objects.get(pk=pk)
    work_experiences = WorkExperience.objects.filter(executive=executive)
    return render(request, 'executives/work_experience_list.html', {
        'work_experiences': work_experiences,
        'executive': executive,
    })


@login_required
def certificate_add(request, pk):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        print('form:', form)
        if form.is_valid():
            certificate = form.save(commit=False)
            executive = Executive.objects.get(pk=pk)
            certificate.executive = executive
            certificate.save()

            messages.success(request, 'Certificate added successfully')
            return redirect('executives:certificate_list', pk=pk)

        print('request is not valid')
    else:
        form = CertificateForm()
    return render(request, 'executives/certificate_add.html', {'form': form})


@login_required
def certificate_edit(request, pk, certificate_pk):
    certificate = get_object_or_404(Certificate, pk=certificate_pk)
    if request.method == 'POST':
        form = CertificateForm(request.POST, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('executives:certificate_list', pk=pk)
    else:
        form = CertificateForm(instance=certificate)
    return render(request, 'executives/certificate_edit.html', {'form': form})


@login_required
def certificate_delete(request, pk, certificate_pk):
    certificate = get_object_or_404(Certificate, pk=certificate_pk)

    if certificate.executive.pk != pk:
        return render(request, 'core/404.html')

    certificate.delete()
    return redirect('executives:certificate_list', pk=pk)


@login_required
def certificate_list(request, pk):
    executive = Executive.objects.get(pk=pk)
    certificates = Certificate.objects.filter(executive=executive)
    return render(request, 'executives/certificate_list.html', {
        'certificates': certificates,
        'executive': executive,
    })



@login_required
def position_consent_add(request, pk):
    if request.method == 'POST':
        form = PositionConsentForm(request.POST)
        print('form:', form)
        if form.is_valid():
            position_consent = form.save(commit=False)
            executive = Executive.objects.get(pk=pk)
            position_consent.executive = executive
            position_consent.save()

            messages.success(request, 'Position consent added successfully')
            return redirect('executives:position_consent_list', pk=pk)

        print('request is not valid')
    else:
        form = PositionConsentForm()
    return render(request, 'executives/position_consent_add.html', {'form': form})


@login_required
def position_consent_edit(request, pk, position_consent_pk):
    position_consent = get_object_or_404(PositionConsent, pk=position_consent_pk)
    if request.method == 'POST':
        form = PositionConsentForm(request.POST, instance=position_consent)
        if form.is_valid():
            form.save()
            return redirect('executives:position_consent_list', pk=pk)
    else:
        form = PositionConsentForm(instance=position_consent)
    return render(request, 'executives/position_consent_edit.html', {'form': form})


@login_required
def position_consent_delete(request, pk, position_consent_pk):
    position_consent = get_object_or_404(PositionConsent, pk=position_consent_pk)

    if position_consent.executive.pk != pk:
        return render(request, 'core/404.html')

    position_consent.delete()
    return redirect('executives:position_consent_list', pk=pk)


@login_required
def position_consent_list(request, pk):
    executive = Executive.objects.get(pk=pk)
    position_consents = PositionConsent.objects.filter(executive=executive)
    return render(request, 'executives/position_consent_list.html', {
        'position_consents': position_consents,
        'executive': executive,
    })



@login_required
def education_add(request, pk):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        print('form:', form)
        if form.is_valid():
            education = form.save(commit=False)
            executive = Executive.objects.get(pk=pk)
            education.executive = executive
            education.save()

            messages.success(request, 'Education added successfully')
            return redirect('executives:education_list', pk=pk)

        print('request is not valid')
    else:
        form = EducationForm()
    return render(request, 'executives/education_add.html', {'form': form})


@login_required
def education_edit(request, pk, education_pk):
    education = get_object_or_404(Education, pk=education_pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('executives:education_list', pk=pk)
    else:
        form = EducationForm(instance=education)
    return render(request, 'executives/education_edit.html', {'form': form})


@login_required
def education_delete(request, pk, education_pk):
    education = get_object_or_404(Education, pk=education_pk)

    if education.executive.pk != pk:
        return render(request, 'core/404.html')

    education.delete()
    return redirect('executives:education_list', pk=pk)


@login_required
def education_list(request, pk):
    executive = Executive.objects.get(pk=pk)
    educations = Education.objects.filter(executive=executive)
    return render(request, 'executives/education_list.html', {
        'educations': educations,
        'executive': executive,
    })
