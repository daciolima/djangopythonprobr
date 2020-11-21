from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from apps.base import urls as base_urls
from apps.aperitivo import urls as aperitivo_urls
from apps.modulos import urls as modulos_urls
from apps.turmas import urls as turmas_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('', include(base_urls), name='home'),
    path('aperitivo/', include(aperitivo_urls)),
    path('modulos/', include(modulos_urls)),
    path('turmas/', include(turmas_urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
