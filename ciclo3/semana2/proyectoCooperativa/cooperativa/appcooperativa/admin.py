from django.contrib import admin

# Register your models here.

from appcooperativa.models import Cliente, Lineas_De_Credito, Credito #se importa las clasesde model
admin.site.register(Cliente)
admin.site.register(Lineas_De_Credito)
admin.site.register(Credito)
