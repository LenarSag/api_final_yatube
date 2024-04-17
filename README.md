# Описание:

Проект "yatube_api" - это социальная сеть, работающая через API, разработанная на основе Django REST framework, предоставляющая функциональность создания сообщений, подписок на других пользователей, обсуждения контента и создания групп с общими интересами.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/LenarSag/api_final_yatube
cd api_final_yatube

Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver

## Документация для API запросов:

Подробная документация для API yatube с примерами доступных запросов и результатов таких запросов доступна после запуска проект по адресу http://127.0.0.1:8000/redoc/

Также, доступна документация в формате .yaml, для этого перейдите в папку /static/ и откройте файл redoc.yaml

## Коллекция запросов для Postman

В директории /postman_collection/ сохранена коллекция запросов для отладки и проверки работы текущей версии API Yatube. Импортируйте коллекцию в Postman и выполняйте запросы. Подробнее о Postman: https://www.postman.com/company/about-postman/