from django.contrib import admin
from .models import *

admin.site.register(type_produit)
admin.site.register(produit)
admin.site.register(fournisseur)
admin.site.register(client)
admin.site.register(bon_commande)
admin.site.register(bon_livraison)
admin.site.register(facture)
admin.site.register(vente)
admin.site.register(stock)
admin.site.register(etablir_BC)
admin.site.register(etablir_BL)
admin.site.register(etablir_facture)
admin.site.register(etablir_vente)
admin.site.register(destocker)
admin.site.register(ajout_stock)









