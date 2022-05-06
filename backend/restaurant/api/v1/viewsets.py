from rest_framework import authentication
from restaurant.models import HotButton, Restaurant
from .serializers import HotButtonSerializer, RestaurantSerializer
from rest_framework import viewsets


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Restaurant.objects.all()


class HotButtonViewSet(viewsets.ModelViewSet):
    serializer_class = HotButtonSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = HotButton.objects.all()
