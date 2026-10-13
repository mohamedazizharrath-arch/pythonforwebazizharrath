from django.contrib import admin

# Register your models here.
from .models import  Vehicule
# Register your models here.
#admin.site.register(Vehicule)
@admin.register(Vehicule)
class vehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible', 'entreprise', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Identification', {
            'fields': ('immatriculation', 'type_vehicule', 'capacite_kg')
        }),
        ('Statut et rattachement', {
            'fields': ('disponible', 'entreprise')
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )