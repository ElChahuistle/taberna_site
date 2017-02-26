from django.contrib import admin
"""from django.forms import TextInput
from django.db import models"""
from .models import Tipo, Pais_de_Origen, Ceveceria, Cerveza, Caracteristica


class PaisDeOrigenAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CervezaAdmin(admin.ModelAdmin):
    list_display = ('name', 'cerveceria', 'existencia')
    fieldsets = [
        (None
            , {'fields': [
                'name'
                , 'cerveceria'
            ]}
         )
        , ('Detalles'
           , {'fields': [
                'tipo'
                , 'grados'
                , 'caracteristicas'
            ]}
        )
        , ('Inventario'
           , {'fields': [
                ('precio_compra', 'precio_venta')
                , 'disponible'
            ]}
        )
    ]

    class Media:
        css = { 'all': ('cerveza_form.css', ) }


class CerveceriaAdmin(admin.ModelAdmin):
    list_display = ('ceveceria', 'pais_de_origen')

admin.site.register(Tipo)
admin.site.register(Pais_de_Origen, PaisDeOrigenAdmin)
admin.site.register(Ceveceria, CerveceriaAdmin)
admin.site.register(Cerveza, CervezaAdmin)
admin.site.register(Caracteristica)
