# Команды работы с minikube

Запустить minikube:

    minikube start --vm-driver=none
    
    minikube addons enable ingress
    minikube addons enable dashboard

Статус minikube:

    minikube status

Остановить minikube:

    minikube stop

Удалить minikube:

    minikube delete

--------------------------------------------------------------------------------

# Команды работы с minikube manifests

Применить yaml-манифест:

    kubectl apply -f ./<file>.yaml
    kubectl apply -f ./<dir>
    kubectl apply -f .

--------------------------------------------------------------------------------

# Команды работы с minikube dashboard

Запустить minikube dashboard:

    minikube dashboard

Вывести minikube dashboard на внешний адрес:

    kubectl proxy --address='0.0.0.0' --port=9000 --disable-filter=true

Доступ к minikube dashboard через браузер:

    http://arch.homework:9000/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/pod?namespace=map

Просмотр всех переменных окружения в консоли:

    printenv
