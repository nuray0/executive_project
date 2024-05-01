from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import about
from dashboard.views import dashboard
from users.views import signup, login, logout

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('accounts/', include('users.urls')),
    path('executives/', include('executives.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
