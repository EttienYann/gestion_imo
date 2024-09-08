from django.db import models

# Create your models here.

class client (models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Proprietaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    num_cni = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.prenom} {self.nom}"  
    
class BienImmobilier(models.Model):
    type_bien = models.CharField(max_length=50)
    adresse = models.CharField(max_length=255)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    prix_location = models.DecimalField(max_digits=10, decimal_places=2)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)

    def __str__(self):
        return  f'{self.adresse} {self.type_bien}'
    
class Location(models.Model):
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        # Remplir automatiquement le prix de vente en fonction du bien immobilier sélectionné
        self.montant = self.bien_immobilier.prix_location
        super(Location, self).save(*args, **kwargs)
    bien_immobilier = models.ForeignKey(BienImmobilier, on_delete=models.CASCADE)
    client = models.ForeignKey(client, on_delete=models.CASCADE)

    def _str_(self):
        return f"Location de {self.client} pour {self.bien_immobilier}"
class Achats(models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    bien_immobilier = models.ForeignKey(BienImmobilier, on_delete=models.CASCADE)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        # Remplir automatiquement le prix de vente en fonction du bien immobilier sélectionné
        self.prix_vente = self.bien_immobilier.prix_vente
        super(Achats, self).save(*args, **kwargs)
    def _str_(self):
        return f"Achat de {self.client} pour {self.bien_immobilier}"

class Contrat(models.Model):
    achats = models.ForeignKey(Achats, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    bien_immobilier = models.ForeignKey(BienImmobilier, on_delete=models.CASCADE)
    client = models.ForeignKey(client, on_delete=models.CASCADE)

    def _str_(self):
        return f"Contrat pour {self.client} sur {self.bien_immobilier}"