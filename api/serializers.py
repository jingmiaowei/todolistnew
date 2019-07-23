from Todo.models import Todolist
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
         model = Todolist
         fields = ('title','finish',)
