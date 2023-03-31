from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import *
from .serializers import *

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET/api'
    ]
    return Response(routes)


@api_view(['GET'])
def getProduct(request):
    product = produit.objects.all()
    serializer = ProductSerializer(product,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addProduct(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getClient(request):
    myClient = client.objects.all()
    serializer = ClientSerializer(myClient,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addClient(request):
    serializer=ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getTypeProduit(request):
    myType = type_produit.objects.all()
    serializer = TypeProduitSerializer(myType,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTypeProduit(request):
    serializer=TypeProduitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getFournisseur(request):
    myFournisseur = fournisseur.objects.all()
    serializer = FournisseurSerializer(myFournisseur,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addFournisseur(request):
    serializer=FournisseurSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


