# Docker сборка контейнеров

Параметры docker файла:

* ENV - переменные окружения
* ARG - переменные во время сборки
* COPY - скопировать файл или папку
* ADD - скопировать файл или папку, скачать по ссылке, разархивировать архив
* EXPOSE - документация
* CMD/ENTRYPOINT - запустить файл/приложение

Режимы работы:

    ENTRYPOINT ping www.google.com

или

    ENTRYPOINT ["ping", "www.google.com"]Docker сборка контейнеров

Комбинированное использование:

    ENTRYPOINT ["ls", "/usr"]
    CMD ["/var"]

--------------------------------------------------------------------------------

# Настройка docker

Авторизация:

    docker login -u "myusername" -p "mypassword" docker.io

Очистка авторизации:

    docker logout

--------------------------------------------------------------------------------

# Команды работы с docker images

Список образов в системе:

    docker images
    
Собрать docker-контейнер:

    docker build -t <username>/<repository>:<version> <path>
    docker build -t <username>/<repository> <path>             [без указания версии проставится тег - latest]

    docker build -f <Dockerfile> -t <username>/<repository>:<version> <path>

Удаление образа из системы:

    docker rmi <id>
    docker rmi faaddba186dc

--------------------------------------------------------------------------------

# Команды работы с docker containers

Загрузить контейнер:

    docker pull <name>

Список запущенных контейнеров:

    docker ps

Список запущенных/остановленных контейнеров:

    docker ps -a
    
Запуск контейнера в console:

    docker run -p <out-port>:<image-port> <name>
    docker run -p 3030:80 nginx
    docker run -it -p 3030:80 nginx

Запуск контейнера в виде daemon:

    docker run -d -p <out-port>:<image-port> <name>
    docker run -d -p <out-port>:<image-port> --name=<docker_name> <name>
    docker run -d -p 3030:80 nginx

Запуск контейнера с параметрами:

    docker run -d -e <var env> -v <mount> -p <out-port>:<image-port> <name>

Просмотр логов запущенного контейнера:

    docker logs <id>
    docker logs -f <id>

Информация о запущенном контейнере:

    docker inspect <id>

Подключение внутрь контейнера:

    docker exec -it <id> bash
    
Остановка запущенного контейнера:

    docker stop <id>
    docker kill <id>

Остановка всех контейнеров:

    docker stop $(docker ps -aq)
    docker kill $(docker ps -aq)

    docker stop $(docker ps -aqf "name=<docker_name>")
    docker kill $(docker ps -aqf "name=<docker_name>")

Удаление остановленного контейнера:

    docker rm <id>
    docker rm faaddba186dc

Удаление всех остановленных контейнеров:

    docker rm $(docker ps -aq)

--------------------------------------------------------------------------------

# Сборка локального проекта

# Создание репозитория

Url:

https://hub.docker.com/repositories -> **Create Repository**

## Сборка docker-контейнера

Сборка docker-контейнера:

    docker build -t kaizent/otus_homework:1.0 .
    docker images

    ??? docker tag kaizent/otus_homework:1.0 kaizent/otus_homework:1.0

    docker push kaizent/otus_homework:1.0
    
    docker run -p 80:8000 kaizent/otus_homework:1.0
    docker run -d -p 80:8000 kaizent/otus_homework:1.0
    docker run -d -p 80:8000 --name=otus_homework kaizent/otus_homework:1.0
