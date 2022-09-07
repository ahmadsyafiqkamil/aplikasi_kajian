from django.contrib import admin
from kajian.models import Kajian, ProgresKajian, Profile, AnggotaKajian


# Register your models here.

class KajianAdmin(admin.ModelAdmin):
    list_display = ('name', 'pj_kajian')


class ProgressAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass

# class AnggotaAdmin(admin.ModelAdmin):
#     list_display = ('kajian', 'anggota')

admin.site.register(Kajian, KajianAdmin)
admin.site.register(ProgresKajian, ProgressAdmin)
admin.site.register(Profile, ProfileAdmin)
# admin.site.register(AnggotaKajian, AnggotaAdmin)
