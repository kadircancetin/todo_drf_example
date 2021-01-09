# About

Very basic django rest framework, todo example with docker.

# Development

```bash
$ sh sh/development_up.sh
```

It will build and start docker container and opens bash shell.

If you want to connect to docker with another terminal:

```bash
$ docker exec -ti todo_example bash
```

In docker:

```bash
$ python manage.py runserver 0:8000  # for run server
$ python manage.py test              # for testing
$ python manage.py createsuperuser   # for generating admin user
```

# Endpoints

```
api/token/
-    gets "username" and "password" returns jwt access and refresh tokens

api/token/refresh/
-    refresh access token via refresh token
```

```
api/todo/
-    GET:
     -    Gets list of todo
-    POST:
    -     Creates new todo
```

```
api/todo/<int:id>
-    GET:
     -    Gets a todo
-    PUT:
    -     Update todo with put request
-    PATCH:
    -     Update todo with patch request
-    DELTE:
    -     Delete related todo
```


# Covearge (%93)

On docker:
```bash
$ pip install coverag
$ coverage run --source='.' manage.py test
$ coverage report
```

```
Name                                    Stmts   Miss  Cover
-----------------------------------------------------------
apps/__init__.py                            0      0   100%
apps/core/models.py                         6      0   100%
apps/core/test.py                          13      0   100%
apps/todos/__init__.py                      0      0   100%
apps/todos/apps.py                          3      3     0%
apps/todos/migrations/0001_initial.py       7      0   100%
apps/todos/migrations/__init__.py           0      0   100%
apps/todos/models.py                       16      0   100%
apps/todos/serializers.py                   7      0   100%
apps/todos/tests/__init__.py                0      0   100%
apps/todos/tests/factories.py              11      0   100%
apps/todos/tests/test_views.py             74      0   100%
apps/todos/views.py                        16      0   100%
apps/users/__init__.py                      0      0   100%
apps/users/apps.py                          3      3     0%
apps/users/tests/__init__.py                0      0   100%
apps/users/tests/factories.py              12      0   100%
apps/users/tests/test_urls.py               0      0   100%
apps/users/tests/test_views.py             19      0   100%
config/__init__.py                          0      0   100%
config/asgi.py                              4      4     0%
config/settings/base.py                    20      0   100%
config/settings/development.py              5      0   100%
config/urls.py                              5      0   100%
config/wsgi.py                              4      4     0%
manage.py                                  12      2    83%
-----------------------------------------------------------
TOTAL                                     237     16    93%
```
