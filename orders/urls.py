from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),  # Menampilkan isi keranjang
    path('add/<int:menu_id>/', views.add_to_cart, name='add'),  # Tambah item ke keranjang
    path('remove/<int:menu_id>/', views.remove_from_cart, name='remove'),  # Hapus seluruh item
    path('clear/', views.clear_cart, name='clear'),  # Kosongkan keranjang
    path('update_quantity/<int:menu_id>/', views.update_quantity, name='update_quantity'),  # Tambah/kurangi/set quantity
    path('confirm/', views.confirm_order, name='confirm'),  # Form konfirmasi pemesan ke WA
    path('form-konfirmasi/', views.confirmation_form, name='confirmation-form'),  # halaman baru
]
