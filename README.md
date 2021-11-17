# Otus
Домашние задания по курсу OTUS -  Microservice Architecture 

Требования:
- приложить инструкцию по разворачиванию приложения
- при сдаче ДЗ использовать хост arch.homework - добавить его в хосты локальной машины
- перед сдачей ДЗ пересоздать kubernetes и перить работоспособность (запушить образ, создание namespace, проверить порты и сервис)

--------------------------------------------------------------------------------

## Домашнее задание №1

Создать минимальный сервис, который:
1. отвечает на порту 8000 
2. имеет http-метод GET /health/ RESPONSE: {"status": "OK"}

Cобрать локально образ приложения в докер.
Запушить образ в **dockerhub**

Написать манифесты для деплоя в **k8s** для этого сервиса.
Манифесты должны описывать сущности **Deployment**, **Service**, **Ingress**. 
В **Deployment** могут быть указаны **Liveness**, **Readiness** пробы. 
Количество реплик должно быть не меньше 2.
**Image** контейнера должен быть указан с **Dockerhub**.
Хост в ингрессе должен быть **arch.homework**.

В итоге после применения манифестов GET запрос на http://arch.homework/health должен отдавать {“status”: “OK”}.

На выходе предоставить:
1. ссылку на github c манифестами. Манифесты должны лежать в одной директории, так чтобы можно было их все применить одной командой kubectl apply -f .
2. url, по которому можно будет получить ответ от сервиса (либо тест в postmanе).

Задание со звездой* (+5 баллов):
В Ingress-е должно быть правило, которое форвардит все запросы с /otusapp/{student name}/* на сервис с rewrite-ом пути. Где {student name} - это имя студента.

## Среда тестирования

Версии компонентов:

* server version  : Ubuntu 20.04.3 LTS (отсутствует виртуализация на сервере)
* docker version  : v20.10.10 (API version: v1.41; containerd version: 1.4.11)
* kubectl version : v1.22.3
* minikube version: v1.24.0 (--vm-driver=none - отсутствует виртуализация на сервере)

## Инструкция по запуску docker

В файл /etc/hosts добавить строчку:

    127.0.0.1    arch.homework

Запустить docker:

    docker run -d -p 80:8000 --name=otus_homework kaizent/otus_homework:1.0

Проверить работоспособность:

    curl -s http://arch.homework/health

Остановить docker:

    docker stop $(docker ps -aqf "name=otus_homework")
    docker rm $(docker ps -aqf "name=otus_homework")

## Инструкция по запуску docker-compose

В файл /etc/hosts добавить строчку:

    127.0.0.1    arch.homework

Запустить compose-контейнер:

    docker-compose up -d

Проверить работоспособность:

    curl -s http://arch.homework/health

Остановить compose-контейнер:

    docker-compose down

## Инструкция по запуску minikube

Запустить minikube:

    minikube start --vm-driver=none
    minikube addons enable ingress

Получить IP сервера minikube:
    
    minikube ip

В файл /etc/hosts добавить строчку с найденным minikube ip:

    <minikube ip>    arch.homework

Применить yaml-манифесты:

    kubectl apply -f ./manifests/namespace.yaml
    kubectl apply -f ./manifests/kubernetes/

Проверить работоспособность:

    curl -s http://arch.homework/
    curl -s http://arch.homework/config
    curl -s http://arch.homework/health
    curl -s http://arch.homework/version

Во вложении postman-коллекция запросов:

* postman_collection.json

--------------------------------------------------------------------------------