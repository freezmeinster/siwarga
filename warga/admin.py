from django.contrib import admin
from .models import Warga

@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    pass
