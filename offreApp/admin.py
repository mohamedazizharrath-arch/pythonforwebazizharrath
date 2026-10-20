from django.contrib import admin

from .models import Offre


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    class PrixFilter(admin.SimpleListFilter):
        title = "tranche de prix"
        parameter_name = "prix"

        def lookups(self, request, model_admin):
            return (
            ('moins_500', "Moins de 500"),
            ('500_1000', "500 à 1000"),
            ('1000_5000', "1000 à 5000"),
            ('plus_5000', "Plus de 5000"),
        )

        def queryset(self, request, queryset):
            valeur = self.value()
            if valeur == 'moins_500':
                return queryset.filter(prix__lt=500)
            if valeur == '500_1000':
                return queryset.filter(prix__gte=500, prix__lt=1000)
            if valeur == '1000_5000':
             return queryset.filter(prix__gte=1000, prix__lt=5000)
            if valeur == 'plus_5000':
                return queryset.filter(prix__gte=5000)
            return queryset
    list_display = ('id', 'expedition', 'transporteur', 'vehicule', 'prix', 'delai_jours', 'statut', 'date_proposition', 'created_at', 'updated_at')
    list_filter = ('statut', 'date_proposition', 'transporteur', 'vehicule', 'expedition',PrixFilter)
    search_fields = ('statut',)
    list_select_related = ('expedition', 'transporteur', 'vehicule')
    readonly_fields = ('date_proposition', 'created_at', 'updated_at')

    fieldsets = (
        ('Proposition', {
            'fields': ('prix', 'delai_jours', 'statut')
        }),
        ('Rattachements', {
            'fields': ('expedition', 'transporteur', 'vehicule')
        }),
        ('Horodatage', {
            'fields': ('date_proposition', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
