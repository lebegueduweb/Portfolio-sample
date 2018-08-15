from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('blog/', include('blog.urls')),
    path('jobs/', include('jobs.urls')),
    path('', RedirectView.as_view(url='/jobs/')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('imelda/', admin.site.urls, name = "admin"),
    path(r'^auth/', include('rest_framework_social_oauth2.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)