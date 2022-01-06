# Команды работы с minikube

Версия minikube:

    minikube version

Версия ip:

    minikube ip

Зайти на виртуалку minikube:

    minikube ssh
    logout (выход из виртуалки)

Посмотреть nods minikube:

    kubectl get nodes

--------------------------------------------------------------------------------

Посмотреть namespaces minikube:

    kubectl get namespaces

Создать namespace minikube:

    kubectl create namespace <name>
    kubectl create namespace map

Установить namespace по умолчанию:

    kubectl config set-context --current --namespace=<name>

Параметры выполения команды:

    -n <name> или --namespace=<name>

--------------------------------------------------------------------------------

Посмотреть все сервисы в указанном namespace: 

    kubectl get all --namespace=<name>
    kubectl get all --namespace=map

--------------------------------------------------------------------------------

Посмотреть все pods в указанном namespace:

    kubectl get pods --namespace=<name>
    kubectl get pods --namespace=<name> --show-labels
    kubectl get pods --namespace=map

Посмотреть все pods в указанном namespace с дополнительными параметрами:

    kubectl get pods --namespace=<name> -o wide
    kubectl get pods --namespace=map -o wide

Посмотреть все pods во всех namespaces:

    kubectl get pods -A

Посмотреть детальные параметры выбранного pod:

    kubectl describe pod --namespace=<name> <pod>

Посмотреть логи выбранного pod:

    kubectl logs --namespace=<name> <pod>

Зайти в консоль выбранного pod:

    kubectl exec -ti --namespace=<name> <pod> -- /bin/bash

Вывести service на локальную машину в указанном namespace:

    kubectl port-forward pod/<yaml-label-pod> <port-local>:<port-pod> --namespace=<name>
    kubectl port-forward pod/<yaml-label-pod> 10000:8000 --namespace=<name>

Удалить pod в указанном namespace:

    kubectl delete pod --namespace=<name> <pod>
    kubectl delete pod --force --namespace=<name> <pod> (удаление в виде kill -9)

--------------------------------------------------------------------------------

Посмотреть все replicasets в указанном namespace:

    kubectl get replicasets --namespace=<name>
    kubectl get replicasets --namespace=map

    kubectl get rs --namespace=<name>
    kubectl get rs --namespace=map

Посмотреть детальные параметры выбранного replicaset в указанном namespace:

    kubectl describe replicasets --namespace=<name> <replicaset> 

Удалить replicaset в указанном namespace:

    kubectl delete replicasets --namespace=<name> <replicaset>

--------------------------------------------------------------------------------

Посмотреть все deployments в указанном namespace:

    kubectl get deployment --namespace=<name>
    kubectl get deployment --namespace=map

Посмотреть историю по deployment в указанном namespace:

    kubectl rollout history --namespace=map deployment/<yaml-label-deployment> <deployment>
    kubectl rollout history --namespace=map deployment/map-api-deployment deployment.apps/map-api

Откатить версию:

    kubectl rollout undo deployment <yaml-label-deployment> --namespace=<name>
    kubectl rollout undo deployment map-api-deployment --namespace=map

Масштабировать deployment в указанном namespace:

    kubectl scale deployment <yaml-label-deployment> --namespace=<name> --replicas=<count>
    kubectl scale deployment map-api-deployment --namespace=map --replicas=4

--------------------------------------------------------------------------------

Посмотреть все services в указанном namespace:

    kubectl get service --namespace=<name>
    kubectl get service --namespace=map

    kubectl get endpoints --namespace=<name>
    kubectl get endpoints  --namespace=map

Получить адрес service в указанном namespace (в yaml-манифесте должна стоять настройка = type: NodePort):

    minikube service <yaml-label-service> --url --namespace=<name>
    minikube service map-api-service --url --namespace=map

Тестирование сервиса:

    curl http://<ip:port>/health

Вывести service на локальную машину в указанном namespace:

    kubectl port-forward service/<yaml-label-service> <port-local>:<port-service> --namespace=<name>
    kubectl port-forward service/map-api-service 10000:8000 --namespace=map

    kubectl port-forward svc/<yaml-label-service> 10000:8000 --namespace=<name>
    kubectl port-forward svc/map-api-service 10000:8000 --namespace=map

Тестирование сервиса на локальной машине:

    curl http://localhost:10000/

--------------------------------------------------------------------------------

Влючить ingress контроллер в составе minikube:

    minikube addons enable ingress

Посмотреть все ingress в указанном namespace:

    ingress kubectl get pods --namespace=<name> | grep ingress
    ingress kubectl get pods --namespace=map | grep ingress

--------------------------------------------------------------------------------

Цикл проверки:

    while true ; do curl http://<ip:port>/health ; echo '\n'; sleep 1; done
