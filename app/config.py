# std
import os

# project
from utils import CONFIG_UNDEFINED
from utils import load_kubernetes_config


def init_os_environ_config():
    config = dict(
        RUN=os.environ.get('RUN', CONFIG_UNDEFINED),
        HOSTNAME=os.environ.get('HOSTNAME', CONFIG_UNDEFINED),
        VERSION=os.environ.get('VERSION', CONFIG_UNDEFINED),
    )

    return config


def init_os_environ_secret():
    secret = dict(
        DATABASE_URI=os.environ.get('DATABASE_URI', '')
    )

    return secret


def load_config():
    if 'RUN' in os.environ:
        config = init_os_environ_config()
        secret = init_os_environ_secret()
    else:
        config, secret = load_kubernetes_config()

    return config, secret
