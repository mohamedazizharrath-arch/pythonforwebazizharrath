from django.contrib import admin

from .models import Expedition
from django.utils import timezone

class RetardFilter(admin.SimpleListFilter):
        title = "en retard "
        parameter_name = "en_retard"

        def lookups(self, request, model_admin):
         return (
            ('oui', 'OUI'),
            ('non', 'NON'),
        )

        def queryset(self, request, queryset):
         aujourdhui = timezone.localdate()
         clotures = ('attribuee', 'livree', 'annulee')
         if self.value() == 'oui':
            return queryset.filter(date_souhaitee__lt=aujourdhui)
         if self.value() == 'non':
               return queryset.exclude(date_souhaitee__lt=aujourdhui)
         return queryset

@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('reference', 'ville_depart', 'ville_arrivee', 'poids_kg', 'date_souhaitee', 'statut', 'entreprise', 'created_at', 'updated_at')
    list_filter = ('statut', 'entreprise', 'ville_depart', 'ville_arrivee', 'date_souhaitee', 'created_at', RetardFilter)
    search_fields = ('reference', 'ville_depart', 'ville_arrivee', 'description')
    list_select_related = ('entreprise',)
    date_hierarchy = 'date_souhaitee'
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Identification', {
            'fields': ('reference', 'statut', 'entreprise')
        }),
        ('Trajet', {
            'fields': ('ville_depart', 'ville_arrivee', 'date_souhaitee')
        }),
        ('Marchandise', {
            'fields': ('poids_kg', 'description')
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    