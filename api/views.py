from Todo.models import Todolist
from rest_framework import generics
from .serializers import PostSerializer

# Create your views here.
class PostAPIView(generics.ListAPIView):
    queryset = Todolist.objects.all()
    serializer_class = PostSerializer

