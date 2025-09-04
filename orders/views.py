from django.shortcuts import render, redirect, get_object_or_404
from menu.models import MenuItem
import urllib.parse

def add_to_cart(request, menu_id):
    # Ambil cart, bisa jadi list of int atau list of dict
    raw_cart = request.session.get('cart', [])

    # Jika masih list of int (struktur lama), ubah ke list of dict dengan quantity=1
    if raw_cart and isinstance(raw_cart[0], int):
        raw_cart = [{'id': i, 'quantity': 1} for i in raw_cart]

    # Periksa apakah item sudah ada
    found = False
    for item in raw_cart:
        if item['id'] == menu_id:
            item['quantity'] += 1
            found = True
            break

    if not found:
        raw_cart.append({'id': menu_id, 'quantity': 1})

    # Simpan kembali ke session
    request.session['cart'] = raw_cart
    request.session.modified = True

    print("ISI CART:", request.session['cart'])
    return redirect('orders:cart')
def remove_from_cart(request, menu_id):
    cart = request.session.get('cart', [])
    
    # Langsung hapus item berdasarkan id
    updated_cart = [item for item in cart if item['id'] != menu_id]

    request.session['cart'] = updated_cart
    request.session.modified = True
    return redirect('orders:cart')
def cart_view(request):
    cart_data = request.session.get('cart', [])
    items = []
    total = 0

    for entry in cart_data:
        menu = get_object_or_404(MenuItem, pk=entry['id'])
        menu.quantity = entry['quantity']
        menu.subtotal = menu.harga * entry['quantity']
        items.append(menu)
        total += menu.subtotal

    # Tambahkan seluruh daftar menu
    all_menu = MenuItem.objects.all()

    message = "Halo, saya ingin pesan:\n"
    for item in items:
        message += f"- {item.nama} x{item.quantity} (Rp {item.subtotal:,})\n"
    message += f"\nTotal: Rp {total:,}"

    wa_link = "https://wa.me/6285706817626?text=" + urllib.parse.quote(message)

    return render(request, 'orders/cart.html', {
        'items': items,
        'total': total,
        'wa_link': wa_link,
        'all_menu': all_menu,  # Untuk form tambah menu di cart.html
    })
from django.views.decorators.http import require_POST

from django.views.decorators.http import require_POST

@require_POST
def update_quantity(request, menu_id):
    cart = request.session.get('cart', [])

    # Konversi jika format lama
    if cart and isinstance(cart[0], int):
        cart = [{'id': i, 'quantity': 1} for i in cart]

    action = request.POST.get('action')
    qty_input = request.POST.get('quantity')

    for item in cart:
        if item['id'] == menu_id:
            if qty_input and not action:
                try:
                    item['quantity'] = max(1, int(qty_input))
                except ValueError:
                    pass
            elif action == 'increase':
                item['quantity'] += 1
            elif action == 'decrease' and item['quantity'] > 1:
                item['quantity'] -= 1
            break

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('orders:cart')

def clear_cart(request):
    request.session['cart'] = []
    return redirect('orders:cart')

def confirm_order(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        catatan = request.POST.get("catatan", "")

        cart = request.session.get("cart", [])
        items = []
        total = 0

        for item in cart:
            menu = MenuItem.objects.get(id=item["id"])
            quantity = item["quantity"]
            total += menu.harga * quantity
            items.append((menu.nama, menu.harga, quantity))

        message = f"Halo, saya ingin memesan:\n"
        for nama_menu, harga, qty in items:
            message += f"- {nama_menu} x{qty} (Rp {harga * qty:,})\n"
        message += f"\nTotal: Rp {total:,}\n"
        message += f"Nama: {nama}\n"
        if catatan:
            message += f"Catatan: {catatan}"

        # NOMOR WA TETAP:
        fixed_nomor = "6285706817626"
        encoded_msg = urllib.parse.quote(message)
        wa_link = f"https://wa.me/{fixed_nomor}?text={encoded_msg}"

        return redirect(wa_link)

    return redirect("orders:cart")

def confirmation_form(request):
    cart = request.session.get("cart", [])
    items = []
    total = 0

    for item in cart:
        menu = MenuItem.objects.get(id=item["id"])
        quantity = item["quantity"]
        total += menu.harga * quantity
        items.append({
            'id': menu.id,
            'nama': menu.nama,
            'harga': menu.harga,
            'quantity': quantity,
            'gambar': menu.gambar,
        })

    return render(request, 'orders/confirmation_form.html', {
        'items': items,
        'total': total,
    })
