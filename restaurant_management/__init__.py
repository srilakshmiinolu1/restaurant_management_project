from django.shortcuts import render
import request
def menu_view(request):
    api_url = 'http://localhost:8000/api/menu/'
    menu_data = []
    try:
        response = request.get(api_url)
        response.raise_for_status()
        menu_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching menu data: {e}")
    content = {
        'menu_items' : menu_data
    }
    return render(request, 'menu.html', context)
            
