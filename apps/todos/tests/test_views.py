from apps.core.test import BaseViewTestCase
from apps.todos.models import Todo
from apps.todos.tests.factories import TodoFactory
from rest_framework import status


class TodoListCreateAPIViewTestCase(BaseViewTestCase):
    def setUp(self):
        self.url = "/api/todo/"

        self.user, self.user_client = self.create_user_and_get_client()
        self.anonym_client = self.get_anonymous_client()

        # user todos
        TodoFactory.create_batch(5, user=self.user)

        # not user todos
        TodoFactory.create_batch(3)

        # test data for create todo
        tmp = TodoFactory()
        self.example_data = {
            "state": tmp.state,
            "title": tmp.title,
            "body": tmp.body,
        }
        tmp.delete()

    def test_not_authorized_on_anonym(self):
        response = self.anonym_client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anonym_client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_get_list_of_todos(self):
        response = self.user_client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_todos = [x["id"] for x in response.data]
        expected_todos = list(
            Todo.objects.filter(user=self.user).order_by("-created_datetime").values_list("id", flat=True)
        )

        self.assertEqual(response_todos, expected_todos)

    def test_create_todo(self):
        response = self.user_client.post(self.url, data=self.example_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        todo_obj = Todo.objects.get(id=response.data['id'])

        self.assertEqual(todo_obj.user, self.user)
        self.assertEqual(todo_obj.state, self.example_data['state'])
