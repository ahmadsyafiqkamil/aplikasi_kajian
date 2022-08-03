from django.contrib import admin
from kajian.models import Kajian


# Register your models here.

class KajianAdmin(admin.ModelAdmin):
    pass


admin.site.register(Kajian, KajianAdmin)
