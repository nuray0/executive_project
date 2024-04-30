from django.contrib import messages
from django.shortcuts import render, redirect

from executives.models import Executive

def dashboard(request):
    executives = Executive.objects.filter(user=request.user)
    return render(request, 'dashboard/index.html', {
        'executives': executives,
    })