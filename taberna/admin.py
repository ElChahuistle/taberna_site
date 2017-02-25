from django.contrib import admin
from .models import Tipo, Pais_de_Origen, Ceveceria, Cerveza, Caracteristica


class PaisDeOrigenAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CervezaAdmin(admin.ModelAdmin):
    list_display = ('name', 'cerveceria', 'precio', 'existencia')


class CerveceriaAdmin(admin.ModelAdmin):
    list_display = ('ceveceria', 'pais_de_origen')

admin.site.register(Tipo)
admin.site.register(Pais_de_Origen, PaisDeOrigenAdmin)
admin.site.register(Ceveceria, CerveceriaAdmin)
admin.site.register(Cerveza, CervezaAdmin)
admin.site.register(Caracteristica)
