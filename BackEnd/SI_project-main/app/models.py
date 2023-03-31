from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator , MaxValueValidator


class type_produit(models.Model):
    code_type = models.AutoField(primary_key=True)
    nom_type = models.CharField(max_length=20 , null=False)
  
    def __str__(self):
       return str(self.nom_type)

class produit(models.Model):
    code_produit = models.AutoField(primary_key=True)
    nom_produit = models.CharField(max_length=30 , null=False)
    type = models.ForeignKey(type_produit, on_delete=models.CASCADE)
    
    def __str__(self):
       return str(self.nom_produit)

class fournisseur(models.Model):
    numero_f = models.AutoField(primary_key=True)
    nom_f = models.CharField(max_length=30 , null=False) 
    prenom_f = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)
    phone = models.IntegerField(unique=True)
    solde=  models.FloatField(blank=True)

    def __str__(self):
       return str(self.nom_f)

class client(models.Model): 
    numero_client = models.AutoField(primary_key=True)
    nom_client = models.CharField(max_length=30 , null=False) 
    prenom_client = models.CharField(max_length=30)
    adresse_clinet = models.CharField(max_length=30)
    phone_client = models.IntegerField( unique=True)
    credit = models.IntegerField(blank=True)

    def __str__(self):
       return str(self.nom_client)

class bon_commande(models.Model):
     code_BC = models.AutoField(primary_key=True)
     Date_BC = models.DateTimeField(default=datetime.now)
     fournisseur = models.ForeignKey(fournisseur , on_delete=models.CASCADE)
     produit = models.ManyToManyField(produit, through='etablir_BC')


class facture(models.Model):
     code_facture = models.AutoField(primary_key=True)
     Date_facture = models.DateTimeField(default=datetime.now)
     taux_remise = models.FloatField(blank=True)
     TVA = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)] , default=19)
     fournisseur = models.ForeignKey(fournisseur , on_delete=models.CASCADE)
     produit = models.ManyToManyField(produit, through='etablir_facture')
  
class bon_livraison(models.Model):
     code_BL = models.AutoField(primary_key=True)
     Date_BL = models.DateTimeField(default=datetime.now)
     taux_remise_BL = models.FloatField(blank=True)  
     fournisseur = models.ForeignKey(fournisseur , on_delete=models.CASCADE)
     produit = models.ManyToManyField(produit, through='etablir_BL')

class stock(models.Model):
    code_stock = models.AutoField(primary_key=True)
    produit_destocke = models.ManyToManyField(produit ,related_name='destock', through='destocker')
    produit_ajoute = models.ManyToManyField(produit , related_name='ajout' , through='ajout_stock')

class vente (models.Model):
    num_vente = models.AutoField(primary_key=True)
    Date_vente = models.DateTimeField(default=datetime.now)
    client = models.ForeignKey(client , on_delete=models.CASCADE)
    produit = models.ManyToManyField(produit, through='etablir_vente')

class etablir_facture (models.Model): 
    facture = models.ForeignKey(facture , on_delete=models.CASCADE)
    produit = models.ForeignKey(produit , on_delete=models.CASCADE)
    prix_unitaire_achat = models.FloatField (null=False)
    prix_unitaire_vente = models.FloatField(null=False)
    qte_produit = models.IntegerField(null = False , blank=False)
    etat = models.BooleanField(default=True)

    class Meta:
        unique_together = [['facture','produit']]


class etablir_BL (models.Model): 
    bon_livraison = models.ForeignKey(bon_livraison , on_delete=models.CASCADE)
    produit = models.ForeignKey(produit , on_delete=models.CASCADE)
    prix_unitaire_achat = models.FloatField (null=False)
    prix_unitaire_vente = models.FloatField(null=False)
    qte_produit = models.IntegerField(null = False , blank=False)
    etat = models.BooleanField(default=True)

    class Meta:
        unique_together = [['bon_livraison','produit']]


class etablir_BC (models.Model): 
    bon_commande = models.ForeignKey(bon_commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(produit , on_delete=models.CASCADE)
    qte_produit = models.IntegerField(null = False , blank=False)

    class Meta:
        unique_together = [['bon_commande','produit']]


class etablir_vente (models.Model): 
    vente = models.ForeignKey(vente , on_delete=models.CASCADE)
    produit = models.ForeignKey(produit , on_delete=models.CASCADE)
    qte_produit = models.IntegerField(null = False , blank=False)
    etat = models.BooleanField(default=True)

    class Meta:
        unique_together = [['vente','produit']]


class destocker (models.Model):
    stock = models.ForeignKey(stock , on_delete=models.CASCADE)
    produit = models.ForeignKey(produit , on_delete=models.CASCADE)
    motif = models.CharField(max_length=50,null = False , blank=False)

    class Meta:
        unique_together = [['stock','produit']]

class ajout_stock (models.Model):
    stock = models.ForeignKey(stock , on_delete=models.CASCADE)
    produit = models.ForeignKey(produit , on_delete=models.CASCADE)
    qte_produit = models.IntegerField(null = False , blank=False)
    prix_unitaire_vente = models.FloatField(null=False)

    class Meta:
        unique_together = [['stock','produit']]




