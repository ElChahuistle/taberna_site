from django.contrib import admin
"""from django.forms import TextInput
from django.db import models"""
from .models import PresentacionCerveza, Tipo, Pais_de_Origen, Ceveceria, Cerveza, Caracteristica


class PaisDeOrigenAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PresentacionCervezasFormAdmin(admin.TabularInline):
    model = PresentacionCerveza
    extra = 1

    def get_max_num(self, request, obj=None, **kwargs):
        return 2


class CervezaAdmin(admin.ModelAdmin):
    list_display = ('name', 'cerveceria',)
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
    ]
    inlines = (PresentacionCervezasFormAdmin, )


class CerveceriaAdmin(admin.ModelAdmin):
    list_display = ('ceveceria', 'pais_de_origen')

admin.site.register(Tipo)
admin.site.register(Pais_de_Origen, PaisDeOrigenAdmin)
admin.site.register(Ceveceria, CerveceriaAdmin)
admin.site.register(Cerveza, CervezaAdmin)
admin.site.register(Caracteristica)
