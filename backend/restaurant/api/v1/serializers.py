from rest_framework import serializers
from restaurant.models import HotButton, Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class HotButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotButton
        fields = "__all__"
