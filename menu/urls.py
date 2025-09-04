from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'menu'  # Penting untuk namespacing

urlpatterns = [
    path('', views.menu_list, name='menu-list'),
    path('tambah/', views.menu_create, name='menu-create'),
    path('edit/<int:pk>/', views.menu_update, name='menu-update'),
    path('hapus/<int:pk>/', views.menu_delete, name='menu-delete'),
]

# Untuk development mode agar bisa akses media (gambar)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
