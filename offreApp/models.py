from django.db import models
import expeditionApp
import vehiculeApp


class Offre(models.Model):
    prix = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    delai_jours = models.PositiveIntegerField()

    statut = models.CharField(
        max_length=20,
    )

    date_proposition = models.DateField(
        auto_now_add=True
    )

    expedition = models.ForeignKey(
        "expeditionApp.Expedition",
        on_delete=models.CASCADE,
        related_name="offres"
    )

    transporteur = models.ForeignKey(
        "entrepriseApp.Utilisateur",
        on_delete=models.CASCADE,
        related_name="offres"
    )

    vehicule = models.ForeignKey(
        "vehiculeApp.Vehicule",
        on_delete=models.CASCADE,
        related_name="offres"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )