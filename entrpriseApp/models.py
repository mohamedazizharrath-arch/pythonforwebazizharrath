from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utilisateur(AbstractUser):
    user_id = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('c', 'chargeur') , ('t', 'tansporteur')], default='c')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=200,blank=False, null=False)
    matricule_fiscale = models.CharField(max_length=17, unique=True)
    type_entreprise = models.CharField(max_length=100, choices=[('c','chargeur'),('t','transporteur')]) 
    adresse = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    geraant = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='entreprise', null=True, blank=True)

    