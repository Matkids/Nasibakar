from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    nama = models.CharField("Nama Menu", max_length=100)
    harga = models.DecimalField("Harga", max_digits=10, decimal_places=2)
    deskripsi = models.TextField("Deskripsi", blank=True, null=True)
    gambar = models.ImageField("Gambar Menu", upload_to='menu/', blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Daftar Menu"
        ordering = ['nama']


class Order(models.Model):
    STATUS_CHOICES = [
        ('menunggu', 'Menunggu Pembayaran'),
        ('diproses', 'Diproses'),
        ('dikirim', 'Dikirim'),
        ('selesai', 'Selesai'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_pesan = models.DateTimeField("Tanggal Pesan", auto_now_add=True)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='menunggu')

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

    class Meta:
        ordering = ['-tanggal_pesan']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Jumlah", default=1)

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.nama}"

    class Meta:
        verbose_name = "Item Pesanan"
        verbose_name_plural = "Daftar Item Pesanan"
