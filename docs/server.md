# Install mc

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install mc

--------------------------------------------------------------------------------

# Install Docker Engine on Ubuntu

Url:

https://docs.docker.com/engine/install/ubuntu/

## Uninstall old versions

    sudo apt-get remove docker docker-engine docker.io containerd runc

## Install using the repository

    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg lsb-release
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

## Install Docker Engine

    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    sudo docker run hello-world

## Connect Docker Engine

    docker login -u "myusername" -p "mypassword" docker.io

--------------------------------------------------------------------------------

# Install Docker compose on Ubuntu

## Install Docker compose

    sudo apt-get install docker-compose

--------------------------------------------------------------------------------

# Install Kubectl Engine on Ubuntu

Url:

https://kubernetes.io/ru/docs/tasks/tools/install-kubectl/

## Install kubectl

    sudo apt-get update && sudo apt-get install -y apt-transport-https
    
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
    
    sudo apt-get update
    sudo apt-get install -y kubectl

## Check bash-completion

    type _init_completion

## Install bash-completion (!!! IF NEED)

    sudo apt-get install bash-completion

--------------------------------------------------------------------------------

# Install Minikube Engine on Ubuntu

Url:

https://kubernetes.io/ru/docs/tasks/tools/install-minikube/
https://kubernetes.io/ru/docs/setup/learning-environment/minikube/
https://minikube.sigs.k8s.io/docs/drivers/none/

Url error "minikube start --vm-driver=none":
    
https://github.com/manusa/actions-setup-minikube/issues/7
https://github.com/manusa/actions-setup-minikube/issues/33
https://stackoverflow.com/questions/61238136/cant-start-minikube-in-ec2-shows-x-sorry-kubernetes-v1-18-0-requires-conntrac

## Install minikube

    curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube
    
    sudo mkdir -p /usr/local/bin/
    sudo install minikube /usr/local/bin/
    
    sudo apt-get install -y conntrack

## Start minikube

    minikube start --vm-driver=none
    
    minikube addons enable ingress
    minikube addons enable dashboard

## Status minikube

    minikube status

## Stop minikube

    minikube stop

## Delete minikube

    minikube delete
