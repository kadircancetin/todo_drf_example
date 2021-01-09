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
```
