from django.http import HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET','PUT','DELETE'])
def index(request):
    return HttpResponse('hi')
