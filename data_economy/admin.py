from django.contrib import admin
from .models import *


# Register your models here.

class DomainAdmin(admin.ModelAdmin):
    pass


class KabDomainAdmin(admin.ModelAdmin):
    pass


class AktifitasUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(AktifitasData, AktifitasUserAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(KabDomain, KabDomainAdmin)
