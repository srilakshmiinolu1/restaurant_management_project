from rest_framework.generics import ListAPIView
from rest_framework import serializers
from .models import MenuCategory
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['name']
class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

