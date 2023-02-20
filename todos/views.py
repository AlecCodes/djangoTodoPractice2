from .models import Todo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    # the main query for the index route
    queryset = Todo.objects.all()
    # the serializer class for serializing output
    serializer_class = TodoSerializer
    #optional permission class for auth
    permission_classes = [permissions.AllowAny]