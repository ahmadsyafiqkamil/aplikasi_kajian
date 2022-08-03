from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Kajian(models.Model):
    nama_kajian = models.CharField(
        max_length=100,
        verbose_name='Name Kajian'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_kajian

    class Meta:  # new
        indexes = [models.Index(fields=["nama_kajian"])]
        ordering = ["-nama_kajian"]
        verbose_name = "kajian"

    def get_absolute_url(self):  # new
        return reverse("detil_kajian", args=[str(self.id)])
