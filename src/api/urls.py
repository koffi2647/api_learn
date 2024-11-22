from django.urls import path
from api.views import api_view


urlpatterns = [
    path('', api_view, name = 'api_view')
]