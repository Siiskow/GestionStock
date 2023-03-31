from rest_framework import serializers
from app.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta : 
        model= produit
        fields='__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta : 
        model= client
        fields='__all__'

class TypeProduitSerializer(serializers.ModelSerializer):
    class Meta : 
        model= type_produit
        fields='__all__'

class FournisseurSerializer(serializers.ModelSerializer):
    class Meta : 
        model= fournisseur
        fields='__all__'