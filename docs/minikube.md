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

Установить namespace по умолчанию:

    kubectl config set-context --current --namespace=<name>

--------------------------------------------------------------------------------

Посмотреть все сервисы в указанном namespace: 

    kubectl get all --namespace=<name>
    kubectl get all --namespace=map

--------------------------------------------------------------------------------

Посмотреть все pods в указанном namespace:

    kubectl get pods --namespace=<name>
    kubectl get pods --namespace=<name> --show-labels
    kubectl get pods --namespace=map

Посмотреть все pods во всех namespaces:

    kubectl get pods -A

Посмотреть детальные параметры выбранного pod:

    kubectl describe pod --namespace=<name> <pod>

Удалить pod в указанном namespace:

    kubectl delete pod --namespace=<name> <pod>

--------------------------------------------------------------------------------

Посмотреть все replicasets в указанном namespace:

    kubectl get rs --namespace=<name>
    kubectl get rs --namespace=map

Удалить replicaset в указанном namespace:

    kubectl delete rs --namespace=<name> <replicaset>

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

Получить адрес service в указанном namespace (в yaml-манифесте должна стоять настройка = type: NodePort):

    minikube service <yaml-label-service> --url --namespace=<name>
    minikube service map-api-service --url --namespace=map

Тестирование сервиса:

    curl http://<ip:port>/health

Вывести service на локальную машину в указанном namespace:

    kubectl port-forward svc/<yaml-label-service> 10000:8000 --namespace=<name>
    kubectl port-forward svc/map-api-service 10000:8000 --namespace=map

Тестирование сервиса на локальной машине:

    curl http://localhost:10000/

--------------------------------------------------------------------------------

Цикл проверки:

    while true ; do curl http://<ip:port>/health ; echo '\n'; sleep 1; done
