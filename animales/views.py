from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Animal
from .serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all().order_by("id")
    serializer_class = AnimalSerializer
    http_method_names = ["get", "post", "put", "delete", "head", "options"]

    def destroy(self, request, *args, **kwargs):
        animal = self.get_object()
        animal.delete()
        return Response({"mensaje": "Animal eliminado correctamente."}, status=status.HTTP_200_OK)
