# cbpq-api
API for the CBPQ Skydive App.

Install [pipenv](https://github.com/evandropomatti/install-pipenv-ubuntu)

Install dependentcies and activate

```sh
pipenv install
pipenv shell
```

```sh
docker pull mysql
docker run --name cbpq-mysql -e MYSQL_ROOT_PASSWORD=<SECRET_PASSWORD> -p 3306:3306 -d mysql:latest
docker exec -it cbpq-mysql mysql -h 127.0.0.1 -P 3306 -u root -p
```
