from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class ProfilAdmin(UserAdmin):
    model = Profil
    fieldsets = UserAdmin.fieldsets + (
        ('Profil ustunlari', {
            'fields': ('tel', 'davlat', "jins", "shahar")
        }),
    )


admin.site.register(Profil, ProfilAdmin)
