import django_filters

from apps.todos.models import Todo


class TodoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="contains")
    body = django_filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Todo
        fields = [
            "title",
            "body",
            "state",
        ]
