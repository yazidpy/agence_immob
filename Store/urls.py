from django.urls import path
from . import views
urlpatterns = [
    path('annonces/',views.AnnonceList.as_view()),
    path('annonce/<int:pk>/',views.AnnonceCreate.as_view()),
    path('property/',views.ListProperty.as_view()),
    path('property/<int:pk>/',views.PropertyItem.as_view()),
    path('property/ground/',views.GroundListCreateView.as_view()),
    path('property/ground/<int:pk>/',views.GroundRetrieveUpdateDestroyView.as_view()),
    path('property/appartement/',views.AppartementListCreateView.as_view()),
    path('property/appartement/<int:pk>/',views.AppartementRetrieveUpdateDestroyView.as_view()),
    path('property/villa/',views.VillaListCreateView.as_view()),
    path('property/villa/<int:pk>/',views.VillaRetrieveUpdateDestroyView.as_view()),
    path('customer/',views.CustomerProfile.as_view()),
    path('customer/<int:pk>/',views.CustomerViewSet.as_view()),
    path('favoris/',views.FavorisList.as_view()),
    path('favoris/<int:pk>/',views.FavorisItem.as_view()),
    path('estimator/appartement/', views.EstimatorView.as_view()),
]
    