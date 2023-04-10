from django.contrib import admin
from .models import *


# Register your models here.

class DomainAdmin(admin.ModelAdmin):
    pass


class KabDomainAdmin(admin.ModelAdmin):
    pass


admin.site.register(Domain, DomainAdmin)
admin.site.register(KabDomain, KabDomainAdmin)
