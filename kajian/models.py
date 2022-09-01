from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    satker = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}-{self.satker}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Kajian(models.Model):
    # slug = models.SlugField(unique=True)
    nama_kajian = models.CharField(
        max_length=100,
        verbose_name='Name Kajian'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pengisi_kajian')
    pj_kajian = models.ForeignKey(User, on_delete=models.CASCADE, related_name='penanggung_jawab_kajian')
    anggota = models.ManyToManyField(User,related_name='anggota_kajian',)

    def __str__(self):
        return self.nama_kajian

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.nama_kajian)
    #     super(Kajian, self).save(*args, **kwargs)

    class Meta:  # new
        indexes = [models.Index(fields=["nama_kajian"])]
        ordering = ["-nama_kajian"]
        verbose_name = "kajian"

    def get_absolute_url(self):  # new
        return reverse("detil_kajian", args=[str(self.id)])


# class KajianAnggota(models.Model):
#     kajian = models.ForeignKey(Kajian,on_delete=models.CASCADE, related_name='id_kajian')
#     anggota = models.ForeignKey(User,on_delete=models.CASCADE,related_name='anggota_kajian')

class ProgresKajian(models.Model):
    kajian = models.ForeignKey('Kajian', on_delete=models.CASCADE)
    progres = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.progres

    class Meta:
        indexes = [models.Index(fields=['kajian'])]
        ordering = ["-kajian"]
        verbose_name = "Progres Kajian"

    def get_absolute_url(self):  # new
        return reverse("detil_progress", args=[str(self.id)])
