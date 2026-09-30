from django.db import models


class Vehicule(models.Model):

    immatriculation = models.CharField(
        max_length=20,
        unique=True
    )

    type_vehicule = models.CharField(
        max_length=20,
        
    )

    capacite_kg = models.PositiveIntegerField()

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
