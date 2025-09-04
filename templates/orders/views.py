from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from urllib.parse import quote
from menu.models import MenuItem

def create_order(request):
    menu_id = request.GET.get('menu_id')
    initial_data = {}

    if menu_id:
        try:
            initial_data['menu'] = MenuItem.objects.get(id=menu_id)
        except MenuItem.DoesNotExist:
            pass

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            pesan = f"Halo, saya {order.nama_pelanggan} ingin memesan {order.jumlah}x {order.menu.nama}. Catatan: {order.catatan}"
            url = f"https://wa.me/6281808882819?text={quote(pesan)}"
            return redirect(url)
    else:
        form = OrderForm(initial=initial_data)

    return render(request, 'orders/order_form.html', {'form': form})
