from django.contrib import admin
from .models import Tipo, Pais_de_Origen, Ceveceria, Cerveza, Caracteristica


admin.site.register(Tipo)
admin.site.register(Pais_de_Origen)
admin.site.register(Ceveceria)
admin.site.register(Cerveza)
admin.site.register(Caracteristica)
