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
    def clean(self):
            super().clean()
            if self.entreprise_id and self.entreprise.type_entreprise != 't':
                raise ValidationError("L'entreprise associée doit être de type 'transporteur'.")  
            if self.vehicule_id and self.vehicule.entreprise_id != self.entreprise_id:
                raise ValidationError("Le véhicule associé à l'offre doit appartenir à la même entreprise que l'offre.")
            if self.expedition_id and self.expedition.statut != 'publie':
                raise ValidationError("L'expédition associée à l'offre doit être publiée pour pouvoir recevoir des offres.")
            if Offre.objects.filter(
                entreprise_id=self.entreprise_id,
                expedition_id=self.expedition_id,
                statut="propose"
            ).exclude(pk=self.pk).exists():
                raise ValidationError("Cette entreprise a déjà une offre proposée pour cette expédition.")
    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

            if self.statut == 'acceptee' and self.expedition_id:
                self.expedition.statut = 'attribuee'
                self.expedition.save()