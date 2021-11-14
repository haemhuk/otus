# std
import os
import yaml


CONFIG_UNDEFINED = 'undefined'
CONFIG_DEFAULT = dict(
    HOSTNAME=os.environ.get('HOSTNAME', 'localhost'),
    VERSION=os.environ.get('VERSION', CONFIG_UNDEFINED),
    YAML='not found'
)


def load_kubernetes_config():
    
    def load_yaml_config(path):
        if not os.path.exists(path):
            return {}

        with open(path, 'r') as stream:
            try:
                config = yaml.safe_load(stream)
                return config.get('data', {})
            except yaml.YAMLError as exc:
                return None

    config_path = '../manifests/kubernetes/app_config.yaml'
    secret_path = '../manifests/kubernetes/app_secret.yaml'

    config = load_yaml_config(config_path)
    secret = load_yaml_config(secret_path)

    if config:
        config['YAML'] = 'load'
    else:
        config = CONFIG_DEFAULT

    config['RUN'] = 'uvicorn'

    if 'HOSTNAME' in os.environ:
        config['HOSTNAME'] = os.environ.get('HOSTNAME')
        config['RUN'] = 'docker'

    if 'HOSTNAME' not in config:
        config['HOSTNAME'] = 'localhost'

    if 'DOCKER_RUN' in os.environ:
        config['RUN'] = os.environ.get('DOCKER_RUN', 'docker')

    return config, secret
