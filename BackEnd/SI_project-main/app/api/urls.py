from django.urls import path
from . import views

urlpatterns = [
  path('getRoutes',views.getRoutes),
  path('getProduct',views.getProduct),
  path('addProduct',views.addProduct),
  path('addClient',views.addClient),
  path('getClient',views.getClient),
  path('addTypeProduit',views.addTypeProduit),
  path('getTypeProduit',views.getTypeProduit),
  path('getFournisseur',views.getFournisseur),
  path('addFournisseur',views.addFournisseur)
]