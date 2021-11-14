# Настройка hosts

В файл /etc/hosts добавить настройку:

    127.0.0.1    arch.homework

--------------------------------------------------------------------------------

# Настройка виртуального окружения

Установка модуля виртуального окружения:

    sudo apt install python3.8-venv

Создание виртуального окружения:

    python3 -m venv ./venv
    source ./venv/bin/activate
    pip install -r requirements.txt

--------------------------------------------------------------------------------

# Запуск сервера

Запуск сервера:

    source ./venv/bin/activate
    uvicorn main:app --reload
    uvicorn main:app --port 8000 --reload

--------------------------------------------------------------------------------