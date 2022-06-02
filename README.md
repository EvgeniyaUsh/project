# project
Social Network

Инструкция для локального запуска проекта:

- склонировать репозиторий - git clone https://github.com/EvgeniyaUsh/project
- зайти в папку проека - cd project
- сбилдить проект - sudo docker-compose build
- поднять контейнеры - sudo docker-compose up
- проект будет доступен по адресу - http://0.0.0.0:8000/

Регистрация по адресу:

по урле http://127.0.0.1:8000/api/registration/ нужно отправить post запрос с именем и паролм в json формате

{
"username" : "Bob",
"password" : "Asdfghj_098"
}

после регистрации необходимо получить токен по урле http://127.0.0.1:8000/api/token/ нужно отправить post запрос с именем и паролм в json формате

{
"username" : "Bob",
"password" : "Asdfghj_098"
}

ответ должен прийти в виде:

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDI4ODEyOSwiaWF0IjoxNjU0MjAxNzI5LCJqdGkiOiI4ZmZjMjU5MDM3MTg0ZWU1OGViMTM3NGY0NTUwOTk5MiIsInVzZXJfaWQiOjV9.g1ITSjoTqq_lx6nQc--AmomSQAV60CXgebpOwIHX-uk",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0Mjg4MTI5LCJpYXQiOjE2NTQyMDE3MjksImp0aSI6IjczOTRkNzVlZjZmOTRiYjhiMjU2OWU1ZTk2NzQyNDk1IiwidXNlcl9pZCI6NX0.wyDh4bylcOSCCu3rk5SwuTLknoZTvsbNclTPmC9miZw"
}

