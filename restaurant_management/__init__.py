from rest_framework.views import APIView
from rest_frmework.response import Rersponse
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer
class MenuItemsByCategory(APIView):
    def get(self, request):
        category = request_params.get('category')
        if category:
            items = MenuItem.objects.filter(category=category)
        else:
            items = MenuItem.objects.all()
            serializer = MenuItemSerializer(items, many=True)
            return Response(serializer.data,status=status.HTTP_200_ OK)
