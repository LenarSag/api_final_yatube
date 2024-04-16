Описание:

Проект "yatube_api" - это социальная сеть, работающая через API, разработанная на основе Django REST framework, предоставляющая функциональность создания сообщений, подписок на других пользователей, обсуждения контента и создания групп с общими интересами.

Как запустить проект:

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




Для взаимодействия с ресурсами применяются такие эндпоинты:
/api/v1/jwt/create/ (POST): передаём логин и пароль, получаем токен.
/api/v1/jwt/refresh/ (POST): обновляем токен.
/api/v1/jwt/refresh/ (POST): проверяем токен.

api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост с идентификатором{post_id}.

api/v1/groups/ (GET): получаем список всех групп.
api/v1/groups/{group_id}/ (GET): получаем информацию о группе с идентификатором {group_id}.

api/v1/posts/{post_id}/comments/
(GET): получаем список всех комментариев поста с идентификатором post_id
(POST): создаём новый комментарий для поста с идентификатором {post_id}.
api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий с идентификатором {comment_id} в посте с id=post_id.

/api/v1/follow/ (GET): возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
/api/v1/follow/ (POST): подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.


Примеры запросов:

Пример POST-запроса с токеном Антона Чехова: добавление нового поста.
POST .../api/v1/posts/
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
} 
Пример ответа:
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
} 
Пример POST-запроса с токеном Антона Чехова: отправляем новый комментарий к посту с id=14.
POST .../api/v1/posts/14/comments/
{
    "text": "тест тест"
} 
Пример ответа:
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
} 
Пример GET-запроса с токеном Антона Чехова: получаем информацию о группе.
GET .../api/v1/groups/2/
Пример ответа:
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
}

Пример GET-запроса с токеном Сергея Пушкина: получаем список подписок.
GET .../api/v1/follow/
Пример ответа:
[
    {
        "user": "Сергей Пушкин",
        "following": "Жорж Дантес"
    },
    {
        "user": "Сергей Пушкин",
        "following": "Александр I"
    },
]

Пример POST-запроса с токеном Сергея Пушкина: подписываемся на другого пользователя.
POST .../api/v1/follow/
{
"following": "Joe Biden"
}

Пример ответа:
[
    {
        "user": "Сергей Пушкин",
        "following": "Joe Biden"
    },
]

Пример POST-запроса Сергея Пушкина: получаем токен.
POST .../api/v1/jwt/create

{
"username": "123456",
"password": "123456"
}

Пример ответа:

{
"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjE3NjMzLCJqdGkiOiJmZTY1Y2FiMWUxM2I0OGI1YjE1NDZmN2Y3YmI3ZmIwZCIsInVzZXJfaWQiOjF9.AEkk4YZKOX4147Pf7Qy5o-KIRctM_Be7FbGtRXfMnSo",
"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjE3NjMzLCJqdGkiOiJmZTY1Y2FiMWUxM2I0OGI1YjE1NDZmN2Y3YmI3ZmIwZCIsInVzZXJfaWQiOjF9.AEkk4YZKOX4147Pf7Qy5o-KIRctM_Be7FbGtRXfMnSo"
}


Пример POST-запроса Сергея Пушкина: обновляем токен.
POST .../api/v1/jwt/create

{
"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjE3NjMzLCJqdGkiOiJmZTY1Y2FiMWUxM2I0OGI1YjE1NDZmN2Y3YmI3ZmIwZCIsInVzZXJfaWQiOjF9.AEkk4YZKOX4147Pf7Qy5o-KIRctM_Be7FbGtRXfMnSo"
}

Пример ответа:
{
"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MjE3NjMzLCJqdGkiOiJmZTY1Y2FiMWUxM2I0OGI1YjE1NDZmN2Y3YmI3ZmIwZCIsInVzZXJfaWQiOjF9.AEkk4YZKOX4147Pf7Qy5o-KIRctM_Be7FbGtRXfMnSo"
}

Пример POST-запроса Сергея Пушкина: проверяем токен.
POST .../api/v1/jwt/verify

{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMzM0NjQ3LCJqdGkiOiJiMzQzYjkwYWNhNTU0ZTIwOTNmZDM5ZTQ2Mzc4ODYyZiIsInVzZXJfaWQiOjN9.xuVNPH8WyQUXv0a6JrIl0F18eqcZ_R7P6fAMCXk60mc"
}

Пример ответа:
{}