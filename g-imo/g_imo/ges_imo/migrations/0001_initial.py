# Generated by Django 5.1 on 2024-08-21 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('cni', models.CharField(max_length=30)),
            ],
        ),
    ]
