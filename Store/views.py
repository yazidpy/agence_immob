from rest_framework import generics
from . import models,serializers
import django_filters
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import   AppartementEstimatorSerializer
from .utils import array_to_dataframe
from .model_loader import load_model
from rest_framework.views import APIView
from rest_framework.response import Response


class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = models.Property
        fields = {
            'price': ['gt','lt'],
            'adress':['icontains'],
            'type_propriete':['exact']
        }
class ListProperty(generics.ListAPIView):
    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyFilter


class AnnonceCreate(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Annonce.objects.all()
    serializer_class = serializers.AnnonceSerializer

class PropertyItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertySerializer

class GroundListCreateView(generics.ListCreateAPIView):
    queryset = models.Ground.objects.all()
    serializer_class = serializers.GroundSerializer


class GroundRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ground.objects.all()
    serializer_class = serializers.GroundSerializer
   

class AppartementListCreateView(generics.ListCreateAPIView):
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer


class AppartementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer
   

class VillaListCreateView(generics.ListCreateAPIView):
    queryset = models.Villa.objects.all()
    serializer_class = serializers.VillaSerializer


class VillaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Villa.objects.all()
    serializer_class = serializers.VillaSerializer
   

class CustomerViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.ProfileSerializer
    

class CustomerProfile(generics.ListCreateAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.ProfileSerializer
    

class AnnonceList(generics.ListCreateAPIView):
    queryset = models.Annonce.objects.all()
    serializer_class = serializers.AnnonceSerializer


class FavorisList(generics.ListCreateAPIView):
    queryset=models.Favoris.objects.all()
    serializer_class=serializers.FavorisSerializer

class FavorisItem(generics.RetrieveDestroyAPIView):
      queryset=models.Favoris.objects.all()
      serializer_class=serializers.FavorisSerializer


class EstimatorView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AppartementEstimatorSerializer(data=request.data)
        if serializer.is_valid():
            input_data = [value for field, value in serializer.validated_data.items()]

            model = load_model()
            feature_names = ['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'waterfront', 'view','condition']
            input_array  = array_to_dataframe(input_data, feature_names)

            serializer.validated_data['price'] = model.predict(input_array)[0]

            return Response(serializer.validated_data)
        else:
            return Response({'error': 'Invalid input data'}, status=400)