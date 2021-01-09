import factory
import factory.fuzzy as fuzzy
from apps.todos.models import Todo
from apps.users.tests.factories import UserFactory


class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo

    user = factory.SubFactory(UserFactory)
    title = factory.Faker("word")
    body = factory.Faker("sentence")
    state = fuzzy.FuzzyChoice(Todo.StateTypes.choices, getter=lambda c: c[0])
