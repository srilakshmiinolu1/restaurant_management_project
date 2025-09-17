class MenuItemsByCategoryView(APIView):
    def get_queryset(slef, request):
        category = request.query_params.get('category',None)
        if category:
            items = MenuItem.objects.filter(category__name__iexact=category)
            else:
                items = MenuItem.objects.all()
                serializer = MenuItemSerializer(items, many=True)
                return Response(serializer.data)   