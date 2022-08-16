from django.contrib import admin
from kajian.models import Kajian, ProgresKajian, Profile


# Register your models here.

class KajianAdmin(admin.ModelAdmin):
    pass


class ProgressAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Kajian, KajianAdmin)
admin.site.register(ProgresKajian, ProgressAdmin)
admin.site.register(Profile, ProfileAdmin)
