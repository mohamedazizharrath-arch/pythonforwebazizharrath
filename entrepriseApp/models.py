from datetime import timezone

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator 
#validators 
def validate_email(value):
    if not value :
        raise ValidationError("L'adresse e-mail ne peut pas être vide.")
    if not value .endswith('@gmail.com'):
        raise ValidationError("L'adresse e-mail doit se terminer par '@gmail.com'.")
matrricule_fiscale_validator = RegexValidator( 
    regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',
    message="matricule errone ."
)
# Create your models here.
class Utilisateur(AbstractUser):
    user_id = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField(unique=True, validators=[validate_email])
    telephone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('c', 'chargeur') , ('t', 'tansporteur')], default='c')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=200,blank=False, null=False)
    matricule_fiscale = models.CharField(max_length=17, unique=True, validators=[matrricule_fiscale_validator])
    type_entreprise = models.CharField(max_length=100, choices=[('c','chargeur'),('t','transporteur')]) 
    adresse = models.TextField(validators=[MinLengthValidator(20,"l'adresse ne peut pas avoir au moins 20 caractères"),MaxLengthValidator(200,"l'adresse ne peut pas avoir plus de 200 caractères")]) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    geraant = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='entreprise', null=True, blank=True)

    @classmethod

    def _generate_reference(cls):
        annee = timezone.now().strftime("%Y")
        prefix = f"{annee}-USER-"
        dernier = (
            #cls.objects.all() #select * from expedition
            cls.objects.filter(reference__startswith=prefix)
            .order_by('user_id')#- pour inverser l'ordre (first)
            .last()
        )
        
        compteur =( int(dernier.reference[-2:]+1) if dernier else 0
        )
        if compteur > 99:
                compteur = 0  
        return f"{prefix}{compteur:02d}"
        
    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        #fct appele pour appliquer validators 
        self.full_clean()  # Valide les champs avant de sauvegarder
        super().save(*args, **kwargs)