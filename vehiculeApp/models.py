from django.db import models
from django.core.validators import   MinValueValidator , MaxValueValidator 

class Vehicule(models.Model):

    immatriculation = models.CharField(
        max_length=20,
        unique=True
    )

    type_vehicule = models.CharField(
        max_length=20,
        
    )

    capacite_kg = models.PositiveIntegerField(validators=[MinValueValidator(1, "La capacité doit être supérieure à 0"), MaxValueValidator(1000, "La capacité ne peut pas dépasser 1000")])

    disponible = models.BooleanField(
        default=True
    )

    entreprise = models.ForeignKey(
         "entrepriseApp.Entreprise",
        on_delete=models.CASCADE,
        related_name="vehicules"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
