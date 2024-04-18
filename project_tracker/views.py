from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Client, Project
from .serializers import UserSerializer, ClientSerializer, ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Client.DoesNotExist:
            return Response({'error': 'Client not found'}, status=404)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
