from django.contrib import admin
from .models import Solicitud

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'solicitante', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')