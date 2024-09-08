from django import forms
from ges_imo.models import client , Proprietaire ,BienImmobilier ,Achats,Contrat,Location

class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ['nom', 'prenom', 'adresse', 'email', 'tel']
class ProprioForm(forms.ModelForm):
    class Meta:
        model = Proprietaire
        fields = ['nom', 'prenom', 'num_cni', 'adresse']

class BienImmobilierForm(forms.ModelForm):
    class Meta:
        model = BienImmobilier
        fields = ['type_bien', 'adresse', 'prix_vente', 'prix_location', 'proprietaire']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['date_debut', 'date_fin', 'bien_immobilier', 'client']
        widgets = {
        'date_debut': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        'date_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }

class AchatsForm(forms.ModelForm):
    class Meta:
        model = Achats
        fields = ['client', 'bien_immobilier']

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = ['achats', 'location', 'bien_immobilier', 'client']