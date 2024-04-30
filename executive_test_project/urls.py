from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import about, index

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('accounts/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('executives/', include('executives.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
