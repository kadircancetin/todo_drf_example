from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.todos.models import Todo
from apps.todos.serializers import TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
