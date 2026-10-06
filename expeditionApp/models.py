from datetime import timezone

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Expedition(models.Model):
    reference = models.CharField(
        max_length=20,
        unique=True
    )

    ville_depart = models.CharField(
        max_length=100
    )

    ville_arrivee = models.CharField(
        max_length=100
    )

    poids_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2, validators=[MinValueValidator(0.01, "Le poids doit être supérieur à 0")]
    )

    date_souhaitee = models.DateField()

    description = models.TextField(
        blank=True
    )

    statut = models.CharField(
        max_length=20,
       
    )

    entreprise = models.ForeignKey(
        "entrepriseApp.Entreprise",
        on_delete=models.CASCADE,
        related_name="expeditions"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'c':
            raise ValidationError("L'entreprise associée doit être de type 'chargeur'.")    
    @classmethod
    def _generate_reference(cls):
        annee = timezone.now().strftime("%Y")
        prefix = f"EXP-{annee}-"
        dernier = (
            #cls.objects.all() #select * from expedition
            cls.objects.filter(reference__startswith=prefix)
            .order_by('reference')#- pour inverser l'ordre (first)
            .last()
        )
        
        compteur =( int(dernier.reference[-5:]+1) if dernier else 1
        )
        if compteur > 99999:
                raise ValueError("Le compteur a dépassé la limite maximale de 99999.")
        return f"{prefix}{compteur:05d}"
        
    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        #fct appele pour appliquer validators 
        self.full_clean()  # Valide les champs avant de sauvegarder
        super().save(*args, **kwargs)