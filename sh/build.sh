git pull origin master;
sudo docker-compose -f docker-compose-base.yml -f docker-compose-production.yml build;
sudo docker-compose -f docker-compose-base.yml -f docker-compose-production.yml kill;
sudo docker-compose -f docker-compose-base.yml -f docker-compose-production.yml up -d;
