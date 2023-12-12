from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class ProfilAdmin(UserAdmin):
    model = Profil
    fieldsets = UserAdmin.fieldsets + (
        ('Profil ustunlari', {
            'fields': ('tel', 'davlat', "jins", "shahar", "tasdiqlash_kodi", "tasdiqlangan", "manzil", "zipcode")
        }),
    )


admin.site.register(Profil, ProfilAdmin)
