from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from .forms import MenuItemForm

def menu_list(request):
    items = MenuItem.objects.all()
    context = {
        'menu_items': items,
        'title': 'Menu Nasi Bakar Bangzoel',
    }
    return render(request, 'menu/menu_list.html', context)


def menu_create(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu:menu-list')
    else:
        form = MenuItemForm()
    return render(request, 'menu/menu_form.html', {'form': form, 'title': 'Tambah Menu'})


def menu_update(request, pk):
    menu = get_object_or_404(MenuItem, pk=pk)
    form = MenuItemForm(request.POST or None, request.FILES or None, instance=menu)
    if form.is_valid():
        form.save()
        return redirect('menu:menu-list')
    return render(request, 'menu/menu_form.html', {'form': form, 'title': 'Edit Menu'})


def menu_delete(request, pk):
    menu = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu:menu-list')
    return render(request, 'menu/menu_confirm_delete.html', {'menu': menu})
