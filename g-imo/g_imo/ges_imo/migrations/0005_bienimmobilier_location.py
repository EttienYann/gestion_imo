# Generated by Django 5.1 on 2024-08-22 02:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ges_imo', '0004_proprietaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='BienImmobilier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_bien', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=255)),
                ('prix_vente', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prix_location', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ges_imo.proprietaire')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bien_immobilier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ges_imo.bienimmobilier')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ges_imo.client')),
            ],
        ),
    ]
