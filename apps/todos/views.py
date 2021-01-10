from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.todos.filters import TodoFilter
from apps.todos.models import Todo
from apps.todos.serializers import TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TodoFilter

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer
    lookup_url_kwarg = "id"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
