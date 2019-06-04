from django.contrib import admin

# Register your models here.

from placas.models import Placa, Item, Modelo_placa

class PlacaAdmin(admin.ModelAdmin):
    list_display = ('id_placa', 'id_modelo')

class ItemAdmin(admin.ModelAdmin):
    list_display = ()

class ModeloAdmin(admin.ModelAdmin):
    list_display = ()

    

admin.site.register(Placa, PlacaAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Modelo_placa, ModeloAdmin)
