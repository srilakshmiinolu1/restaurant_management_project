from rest_framework import serializers
class MenuItem(serializers.serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_degits=5, decimal_places=2)
    
