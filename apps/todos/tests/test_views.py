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
        TodoFactory.create_batch(5, user=self.user, title="test title")

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

    def test_filter_on_list(self):
        response = self.user_client.get(self.url, data={"title": "xix"*10})
        self.assertEqual(len(response.data), 0)

        response = self.user_client.get(self.url, data={"title": "test title"})
        self.assertEqual(len(response.data), 5)

        response = self.user_client.get(self.url, data={"title": "test"})
        self.assertEqual(len(response.data), 5)

    def test_create_todo(self):
        response = self.user_client.post(self.url, data=self.example_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        todo_obj = Todo.objects.get(id=response.data["id"])

        self.assertEqual(todo_obj.user, self.user)
        self.assertEqual(todo_obj.state, self.example_data["state"])


class TodoRetrieveUpdateDestroyAPIViewTestCase(BaseViewTestCase):
    def setUp(self):
        self.base_url = "/api/todo/{}"
        self.user, self.user_client = self.create_user_and_get_client()
        self.anonym_client = self.get_anonymous_client()

        self.todo = TodoFactory(user=self.user)
        self.todo_url = self.base_url.format(self.todo.id)

        self.not_user_todo = TodoFactory()
        self.not_user_todo_url = self.base_url.format(self.not_user_todo.id)

    def test_authorization_for_anonym(self):
        response = self.anonym_client.get(self.todo_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anonym_client.patch(self.todo_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anonym_client.put(self.todo_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.anonym_client.delete(self.todo_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorization_for_not_owned_todo(self):
        response = self.user_client.get(self.not_user_todo_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.user_client.patch(self.not_user_todo_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.user_client.put(self.not_user_todo_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.user_client.delete(self.not_user_todo_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_a_todo(self):
        response = self.user_client.get(self.todo_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        check_fields = ["id", "title", "body", "state"]

        for field in check_fields:
            self.assertEqual(response.data[field], getattr(self.todo, field), f"{field} is not same")

    def test_delete_todo(self):
        response = self.user_client.delete(self.todo_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())

    def test_update_todo(self):
        new_title = "test_title"

        response = self.user_client.patch(self.todo_url, data={"title": new_title})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, new_title)
