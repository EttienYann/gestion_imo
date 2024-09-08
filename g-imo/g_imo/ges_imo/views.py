from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpRequest
from ges_imo.models import  client,Proprietaire,Location,Achats,Contrat,BienImmobilier
from ges_imo.form import ClientForm , ProprioForm,AchatsForm,ContratForm,LocationForm , BienImmobilierForm
# Create your views here.
def home(request):
    return render(request,'listing/index.html',{})


def properties(request):
    return render(request, 'listing/properties.html')

def property_details(request):
    return render(request, 'listing/property_details.html')

def contact(request):
    return render(request, 'listing/contact.html')

def dash (request):
    return render(request , 'listing/dash.html')


def client_view (request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    else:
        form = ClientForm()

    clients = client.objects.all()
    total_clients = clients.count()
    return render(request ,'listing/client.html',{'form': form, 'clients': clients , 'total_clients':total_clients} )

def proprio_view(request):
    if request.method == 'POST':
        form = ProprioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proprio')
    else:
        form = ProprioForm()

    proprietaires = Proprietaire.objects.all()
    return render(request, 'listing/proprietaire.html', {'form': form, 'proprietaires': proprietaires})

# Vue pour les biens immobiliers
def bien_view(request):
    if request.method == 'POST':
        form = BienImmobilierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bien')
    else:
        form = BienImmobilierForm()

    biens = BienImmobilier.objects.all()
    return render(request, 'listing/bien.html', {'form': form, 'biens': biens})

# Vue pour les achats
def achats_view(request):
    if request.method == 'POST':
        form = AchatsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('achats')
    else:
        form = AchatsForm()

    achats = Achats.objects.all()
    return render(request, 'listing/achats.html', {'form': form, 'achats': achats})

# Vue pour les locations
def location_view(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location')
    else:
        form = LocationForm()

    locations = Location.objects.all()
    return render(request, 'listing/location.html', {'form': form, 'locations': locations})

# Vue pour les contrats
def contrat_view(request):
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contrat')
    else:
        form = ContratForm()

    contrats = Contrat.objects.all()
    return render(request, 'listing/contrat.html', {'form': form, 'contrats': contrats})

def supprimer_achat(request, achat_id):
    achat = get_object_or_404(Achats, id=achat_id)

    if request.method == 'POST':
        achat.delete()
        return redirect('achats')

    return render(request, 'listing/confirm_delete.html', {'achat': achat})
def modifier_location(request, location_id):
    # Récupérer l'instance de la location à modifier
    location = get_object_or_404(Location, id=location_id)

    # Si le formulaire est soumis (en méthode POST)
    if request.method == 'POST':
        # Le formulaire contient les nouvelles données envoyées par l'utilisateur
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()  # Enregistrer les modifications
            return redirect('location')  # Rediriger vers la liste des locations après modification
    else:
        # Pré-remplir le formulaire avec les données existantes
        form = LocationForm(instance=location)

    # Afficher la page de modification avec les anciennes valeurs dans le formulaire
    return render(request, 'listing/modifier_location.html', {'form': form, 'location': location})

def supprimer_location(request , location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        location.delete()
        return redirect('achats')

    return render(request, 'listing/confirm_delete_l.html', {'location': location})