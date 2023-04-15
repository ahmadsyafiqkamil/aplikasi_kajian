import uuid
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from ajax_datatable.utils import format_datetime


# Create your models here.
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


class AktifitasData(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField(verbose_name="Data")


class Domain(models.Model):
    domain_id = models.CharField(max_length=4, verbose_name="domain_id", primary_key=True)
    domain_name = models.CharField(max_length=250, null=True, blank=True)
    domain_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.domain_name)

    class Meta:
        db_table = "tbl_domain"


class KabDomain(models.Model):
    domain_id = models.CharField(max_length=4, verbose_name="domain_id", primary_key=True)
    domain_name = models.CharField(max_length=250, null=True, blank=True)
    domain_url = models.CharField(max_length=250, null=True, blank=True)
    domain_domain_id = models.ForeignKey(Domain, on_delete=models.CASCADE, verbose_name="domain dari domain")

    def __str__(self):
        return str(self.domain_name)

    class Meta:
        db_table = "tbl_kab_domain"


class SubjectCategory(models.Model):
    subcat_id = models.CharField(max_length=4, verbose_name="subcat_id", primary_key=True)
    title = models.CharField(max_length=250, null=True, blank=True)


class Subject(models.Model):
    sub_id = models.IntegerField(verbose_name="sub_id", primary_key=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    subcat_id = models.ForeignKey(SubjectCategory, on_delete=models.CASCADE)
    subcat = models.CharField(max_length=250, null=True, blank=True)
    ntabel = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title + " (" + self.subcat + ")"


class Variable(models.Model):
    var_id = models.IntegerField(verbose_name="var_id", primary_key=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=250, null=True, blank=True)
    def_name = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    vertical = models.CharField(max_length=250, null=True, blank=True)
    unit = models.CharField(max_length=250, null=True, blank=True)
    graph_id = models.CharField(max_length=250, null=True, blank=True)
    graph_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title + " (" + self.sub_name + ")"


class Vervar(models.Model):
    kode_ver_id = models.IntegerField(verbose_name="kode_ver_id", null=True, blank=True)
    vervar = models.CharField(max_length=500, null=True, blank=True)
    item_ver_id = models.CharField(max_length=10, null=True, blank=True)
    group_ver_id = models.CharField(max_length=10, null=True, blank=True)
    name_group_ver_id = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.vervar + " (" + self.name_group_ver_id + ")"


class Turth(models.Model):
    turth_id = models.IntegerField(verbose_name="turth_id", null=True, blank=True)
    turth = models.CharField(max_length=250, null=True, blank=True)
    group_turth_id = models.CharField(max_length=10, null=True, blank=True)
    name_group_turth = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.turth + " (" + self.name_group_turth + ")"


class Unit(models.Model):
    unit_id = models.IntegerField(verbose_name="unit_id", null=True, blank=True)
    unit = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.unit


class Period(models.Model):
    th_id = models.IntegerField(verbose_name="th_id", null=True, blank=True)
    th = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.th_id
