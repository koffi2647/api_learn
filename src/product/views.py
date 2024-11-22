from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view


from product.serializer import ProductSerializer

# Create your views here.
@api_view(['GET'])
def api_view(request):
    #request est une instance de la classe httprequest
    #requests est une librairie qui permet de construire des clients 
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        # data['name'] = query.name
        # data['content'] = query.content
        data = ProductSerializer(query).data
        # data['price'] = query.price
    return Response(data)
