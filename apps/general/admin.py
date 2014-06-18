from django.contrib import admin
from .models import Equipo, Grupo, Encuentro

# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
	list_filter = ('grupo',)

class EncuentroAdmin(admin.ModelAdmin):
	list_filter = ('local__grupo',)

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Grupo)
admin.site.register(Encuentro, EncuentroAdmin)