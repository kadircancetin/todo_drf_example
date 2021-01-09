docker-compose -f docker-compose-base.yml -f docker-compose-development.yml kill;
docker-compose -f docker-compose-base.yml -f docker-compose-development.yml up --build -d;
docker exec -ti todo_example bash;
