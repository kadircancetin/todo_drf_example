from rest_framework import serializers

from apps.todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Todo
        fields = ["id", "user", "title", "body", "state"]
