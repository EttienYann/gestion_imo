"""
URL configuration for g_imo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ges_imo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home , name= 'home'), 
    path('properties/', views.properties, name='properties'),
    path('property-details/', views.property_details, name='property_details'),
    path('contact/', views.contact, name='contact'),
    path('dash/', views.dash , name= 'dash'),
    path('dash/clients',views.client_view , name='client'),
    path('dash/proprietaire',views.proprio_view , name='proprio'),
    path('dash/biens',views.bien_view , name='bien'),
    path('dash/achats',views.achats_view, name='achats'),
    path('dash/location',views.location_view , name='location'),
    path('dash/contrat',views.contrat_view , name='contrat'),
    path('achats/supprimer/<int:achat_id>/', views.supprimer_achat, name='supprimer_achat'),
    path('location/modifier/<int:location_id>/', views.modifier_location, name='modifier_location'),
    path('location/suprimer/<int:location_id>/', views.supprimer_location, name='supprimer_location'),









]
