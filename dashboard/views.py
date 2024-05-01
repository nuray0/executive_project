from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from executives.models import Executive

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        executives = Executive.objects.filter(user=request.user)
        return render(request, 'dashboard/dashboard.html', {
            'executives': executives,
        })
    else:
        return redirect('about')