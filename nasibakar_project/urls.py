from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin (kamu pakai custom url /dashboardku/)
    path('dashboardku/', admin.site.urls),

    # Aplikasi kamu
    path('', include('menu.urls')),
    path('orders/', include('orders.urls')),
]

# Hanya aktif saat DEBUG=True (development)
if settings.DEBUG:
    # Static files bawaan Django (admin, dll.)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Media files (upload user, dll.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
