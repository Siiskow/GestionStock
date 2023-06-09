# Generated by Django 4.1.5 on 2023-01-22 15:12

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ajout_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte_produit', models.IntegerField()),
                ('prix_unitaire_vente', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='bon_commande',
            fields=[
                ('code_BC', models.AutoField(primary_key=True, serialize=False)),
                ('Date_BC', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='bon_livraison',
            fields=[
                ('code_BL', models.AutoField(primary_key=True, serialize=False)),
                ('Date_BL', models.DateTimeField(default=datetime.datetime.now)),
                ('taux_remise_BL', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('numero_client', models.AutoField(primary_key=True, serialize=False)),
                ('nom_client', models.CharField(max_length=30)),
                ('prenom_client', models.CharField(max_length=30)),
                ('adresse_clinet', models.CharField(max_length=30)),
                ('phone_client', models.IntegerField(unique=True)),
                ('credit', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='destocker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='etablir_facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix_unitaire_achat', models.FloatField()),
                ('prix_unitaire_vente', models.FloatField()),
                ('qte_produit', models.IntegerField()),
                ('etat', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='etablir_vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte_produit', models.IntegerField()),
                ('etat', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='fournisseur',
            fields=[
                ('numero_f', models.AutoField(primary_key=True, serialize=False)),
                ('nom_f', models.CharField(max_length=30)),
                ('prenom_f', models.CharField(max_length=30)),
                ('adresse', models.CharField(max_length=30)),
                ('phone', models.IntegerField(unique=True)),
                ('solde', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='produit',
            fields=[
                ('code_produit', models.AutoField(primary_key=True, serialize=False)),
                ('nom_produit', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='type_produit',
            fields=[
                ('code_type', models.AutoField(primary_key=True, serialize=False)),
                ('nom_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='vente',
            fields=[
                ('num_vente', models.AutoField(primary_key=True, serialize=False)),
                ('Date_vente', models.DateTimeField(default=datetime.datetime.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('produit', models.ManyToManyField(through='app.etablir_vente', to='app.produit')),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('code_stock', models.AutoField(primary_key=True, serialize=False)),
                ('produit_ajoute', models.ManyToManyField(related_name='ajout', through='app.ajout_stock', to='app.produit')),
                ('produit_destocke', models.ManyToManyField(related_name='destock', through='app.destocker', to='app.produit')),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.type_produit'),
        ),
        migrations.CreateModel(
            name='facture',
            fields=[
                ('code_facture', models.AutoField(primary_key=True, serialize=False)),
                ('Date_facture', models.DateTimeField(default=datetime.datetime.now)),
                ('taux_remise', models.FloatField(blank=True)),
                ('TVA', models.IntegerField(default=19, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fournisseur')),
                ('produit', models.ManyToManyField(through='app.etablir_facture', to='app.produit')),
            ],
        ),
        migrations.AddField(
            model_name='etablir_vente',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit'),
        ),
        migrations.AddField(
            model_name='etablir_vente',
            name='vente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vente'),
        ),
        migrations.AddField(
            model_name='etablir_facture',
            name='facture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.facture'),
        ),
        migrations.AddField(
            model_name='etablir_facture',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit'),
        ),
        migrations.CreateModel(
            name='etablir_BL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix_unitaire_achat', models.FloatField()),
                ('prix_unitaire_vente', models.FloatField()),
                ('qte_produit', models.IntegerField()),
                ('etat', models.BooleanField(default=True)),
                ('bon_livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bon_livraison')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit')),
            ],
            options={
                'unique_together': {('bon_livraison', 'produit')},
            },
        ),
        migrations.CreateModel(
            name='etablir_BC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte_produit', models.IntegerField()),
                ('bon_commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bon_commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit')),
            ],
            options={
                'unique_together': {('bon_commande', 'produit')},
            },
        ),
        migrations.AddField(
            model_name='destocker',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit'),
        ),
        migrations.AddField(
            model_name='destocker',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stock'),
        ),
        migrations.AddField(
            model_name='bon_livraison',
            name='fournisseur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fournisseur'),
        ),
        migrations.AddField(
            model_name='bon_livraison',
            name='produit',
            field=models.ManyToManyField(through='app.etablir_BL', to='app.produit'),
        ),
        migrations.AddField(
            model_name='bon_commande',
            name='fournisseur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fournisseur'),
        ),
        migrations.AddField(
            model_name='bon_commande',
            name='produit',
            field=models.ManyToManyField(through='app.etablir_BC', to='app.produit'),
        ),
        migrations.AddField(
            model_name='ajout_stock',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit'),
        ),
        migrations.AddField(
            model_name='ajout_stock',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.stock'),
        ),
        migrations.AlterUniqueTogether(
            name='etablir_vente',
            unique_together={('vente', 'produit')},
        ),
        migrations.AlterUniqueTogether(
            name='etablir_facture',
            unique_together={('facture', 'produit')},
        ),
        migrations.AlterUniqueTogether(
            name='destocker',
            unique_together={('stock', 'produit')},
        ),
        migrations.AlterUniqueTogether(
            name='ajout_stock',
            unique_together={('stock', 'produit')},
        ),
    ]
