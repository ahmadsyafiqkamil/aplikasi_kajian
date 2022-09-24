import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from ajax_datatable.utils import format_datetime
from .validator import validate_file_extension


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


def _upload_path(instance, filename):
    return instance.get_upload_path(filename)


class BaseModel(models.Model):
    """
    Base class for all models;
    defines common metadata
    """

    class Meta:
        abstract = True
        ordering = ('-created',)  # better choice for UI
        get_latest_by = "-created"

    # Primary key
    id = models.UUIDField('id', default=uuid.uuid4, primary_key=True, unique=True,
                          null=False, blank=False, editable=False)
    name = models.CharField(null=False, blank=False, max_length=256)
    url = models.CharField(null=False, blank=True, max_length=256)

    # metadata
    created = models.DateTimeField(_('created'), null=True, blank=True, )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        'created by'), null=True, blank=True, related_name='+', on_delete=models.SET_NULL)
    updated = models.DateTimeField(_('updated'), null=True, blank=True, )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        'updated by'), null=True, blank=True, related_name='+', on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)

    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %
                       (self._meta.app_label, self._meta.model_name), args=(self.id,))

    def get_absolute_url(self):
        return self.get_admin_url()

    def created_display(self):
        return format_datetime(self.created)

    created_display.short_description = _('Created')
    created_display.admin_order_field = 'created'

    def updated_display(self):
        return format_datetime(self.updated)

    updated_display.short_description = _('Updated')
    updated_display.admin_order_field = 'updated'

    def save(self, *args, **kwargs):
        today = timezone.now()
        if self.created is None:
            self.created = today
        self.updated = today
        return super(BaseModel, self).save(*args, **kwargs)


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fungsi = models.CharField(max_length=100)
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


class Kajian(BaseModel):
    # nama_kajian = models.CharField(max_length=100, verbose_name='Name Kajian')
    pj_kajian = models.ForeignKey(User, on_delete=models.CASCADE, related_name='penanggung_jawab_kajian')
    anggota = models.ManyToManyField(User, related_name='anggota_kajian', through='AnggotaKajian',
                                     through_fields=('kajian', 'anggota'), )
    uraian_singkat = models.CharField(max_length=150, verbose_name='Uraian Singkat', null=True, blank=True)
    abstrak = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=_upload_path, validators=[validate_file_extension], null=True, blank=True)

    # status = models.IntegerChoices()

    class Meta:
        db_table = "tbl_kajian"

    def get_upload_path(self, filename):
        return "document/" + str(self.created_by) + "/" + filename


class AnggotaKajian(models.Model):
    kajian = models.ForeignKey(Kajian, on_delete=models.CASCADE)
    anggota = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_anggota_kajian"

    # def __str__(self):
    #     return str(self.kajian.pk)


class ProgresKajian(BaseModel):
    kajian = models.ForeignKey('Kajian', on_delete=models.CASCADE)
    progres = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=_upload_path, validators=[validate_file_extension], null=True, blank=True)

    class Meta:
        db_table = "tbl_progress_kajian"

    def get_upload_path(self, filename):
        return "document/" + str(self.kajian.created_by) + "/" + filename


class KomenProgresKajian(BaseModel):
    progres = models.ForeignKey(ProgresKajian, on_delete=models.CASCADE)
    komentar = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=_upload_path, validators=[validate_file_extension], null=True, blank=True)

    def get_upload_path(self, filename):
        return "document/" + str(self.progres.kajian.created_by) + "/" + filename

    class Meta:
        db_table = "tbl_komen_progres_kajian"
