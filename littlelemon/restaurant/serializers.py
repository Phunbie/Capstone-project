from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title','price','inventory']

class BookingSerializer(serializers.ModelSerializer):
        model = Booking
        fields = '__all__'