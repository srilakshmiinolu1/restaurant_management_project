from django.db import models
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    from rest_framework import serializers
    from .models import MenuItem
    class MenuItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = MenuItem
            fields = ['id', 'name', 'description', 'price']
from rest_framework import viewests, filters
from rest_framework.pagination import pageNumberPagination
from .models import MenuItem
from .serializers import MenuItemSerializer
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializers_class = MenuItemSerializer
    filter_backends = [filters.SearchFilter]
    serach_fields = ['name']
    pagination_class = StandardResulttsPagination
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet
router = DefaultRouter()
router .register(r'menu-items', MenuItemViewSet, basename='menuitem')
urlpatterns = [path('', include(router.urls)),]
      