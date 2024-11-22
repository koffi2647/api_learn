from django.http import JsonResponse


def api_view(request, *args, **kwargs):
    data = {
        'name': 'koffi',
        'age': 30,
        'city': 'Paris',
        'country': 'France'
    }
    return JsonResponse(data)
    
