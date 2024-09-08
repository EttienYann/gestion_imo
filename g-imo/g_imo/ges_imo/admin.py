from django.contrib import admin

# Register your models here.
from ges_imo.models import client 
from ges_imo.models import Proprietaire 
from ges_imo.models import Achats
from ges_imo.models import Location
from ges_imo.models import Contrat
from ges_imo.models import BienImmobilier




admin.site.register(client)
admin.site.register(Proprietaire)
admin.site.register(Achats)
admin.site.register(Location)
admin.site.register(Contrat)
admin.site.register(BienImmobilier) 

class ClientAdmin(admin.ModelAdmin):
    search_fields = ['nom', 'prenom', 'email']
class BienImmobilierAdmin(admin.ModelAdmin):
    list_filter = ['type_bien', 'prix_vente']
class LocationAdmin(admin.ModelAdmin):
    list_display = ['client', 'bien_immobilier', 'date_debut', 'date_fin']
