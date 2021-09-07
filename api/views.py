from django.shortcuts import render
from .models import Image
from .serializers import ImageSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(detail=False, methods=['GET'])
    def hello(self, request):
        return render(request, 'home.html')
    
    @action(detail=False, methods=['POST', 'PUT'])
    def postdata(self, request):
        import ipdb
        ipdb.set_trace()
        request.data.pop('csrfmiddlewaretoken')
        Image.objects.create(**request.data)
