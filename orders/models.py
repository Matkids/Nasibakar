# orders/models.py
from django.db import models

class Order(models.Model):
    nama_pemesan = models.CharField(max_length=100)
    no_wa = models.CharField(max_length=15)
    catatan = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_pemesan
