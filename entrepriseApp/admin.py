
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Entreprise, Utilisateur
from vehiculeApp.models import Vehicule
admin.site.site_header = "Administration Transport"  
admin.site.site_title = "Transport Admin"              
admin.site.index_title = "Gestion des expéditions" 
class VehiculeInline(admin.TabularInline):
    model = Vehicule
    extra = 0
    fields = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible')
    show_change_link = True
@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('raison_sociale', 'matricule_fiscale', 'type_entreprise', 'geraant')
    list_filter = ('type_entreprise',)
    search_fields = ('raison_sociale', 'matricule_fiscale')
    inlines = [VehiculeInline]

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ('user_id', 'username', 'email', 'is_active', 'is_superuser', 'role')
    list_editable = ('is_active', 'is_superuser')
    list_display_links = ('user_id', 'username')
    search_fields = ('user_id', 'username', 'email')
    list_filter = ('is_active', 'is_superuser', 'role')
    list_per_page = 20

    # Formulaire de modification
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email')}),
        ('Rôle', {'fields': ('role',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Formulaire de création
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

