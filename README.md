# Udemy-Study

 This repository is built upon the [Udemy Course](https://www.udemy.com/course/django-python-advanced/) in order to enhance the knowledge of django rest framework

# Commands for docker

commands for django application container
```
docker-compose up 
docker-compose run --rm app python3 manage.py test
docker-compose run --rm app python3 flake8
docker-compose run --rm app python3 
docker-compose run --rm app python3 manage.py makemigrations
docker-compose run --rm app python3 migrate
docker-compose run web python3 manage.py createsuperuser
docker-compose down --volume
```

commands for Docker
```
docker system prune -a
docker volume prune
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```


