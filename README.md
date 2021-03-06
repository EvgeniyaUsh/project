# project
Social Network

### Инструкция для локального запуска проекта:

- склонировать репозиторий - git clone https://github.com/EvgeniyaUsh/project
- зайти в папку проекта - cd project
- установить docker-compose - pip install docker-compose
- сбилдить проект - sudo docker-compose build
- поднять контейнеры - sudo docker-compose up
- проект будет доступен по адресу - http://0.0.0.0:8000/

### Регистрация по адресу:

по урле http://127.0.0.1:8000/api/registration/ нужно отправить post запрос с именем и паролем в json формате

{
"username" : "Bob",
"password" : "Asdfghj_098"
}

после регистрации необходимо получить токен по урле http://127.0.0.1:8000/api/token/ нужно отправить post запрос с именем и паролем в json формате

{
"username" : "Bob",
"password" : "Asdfghj_098"
}

ответ должен прийти в виде:

{

    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDI4ODEyOSwiaWF0IjoxNjU0MjAxNzI5LCJqdGkiOiI4ZmZjMjU5MDM3MTg0ZWU1OGViMTM3NGY0NTUwOTk5MiIsInVzZXJfaWQiOjV9.g1ITSjoTqq_lx6nQc--AmomSQAV60CXgebpOwIHX-uk",
    
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0Mjg4MTI5LCJpYXQiOjE2NTQyMDE3MjksImp0aSI6IjczOTRkNzVlZjZmOTRiYjhiMjU2OWU1ZTk2NzQyNDk1IiwidXNlcl9pZCI6NX0.wyDh4bylcOSCCu3rk5SwuTLknoZTvsbNclTPmC9miZw"
}

где access токен будет использоваться для создания/редактирования постов (post/patch запросов) по урле http://127.0.0.1:8000/api/posts/

срок жизни токена задается в настройках (на данный момент установлен 1 день)

после окончания действия access токена, необходимо воспользоваться refresh токеном.
по урле http://127.0.0.1:8000/api/token/refresh/ отправить post запрос с полученным refresh токеном в json формате, в ответ вернется новый access токен, который будет действителен 1 сутки (время жизни refresh токена также можно задавать в настройках)

### Создание поста.

После регистрации и получения access токена по урле http://127.0.0.1:8000/api/posts/ будет доступно создание/редактирование поста.

Для создания необходимо отправить post запрос с данными в json формате, пример:

{
"header" : "Название поста",
"text" : "Содержимое поста"
}

в ответ прийдет json в виде:

{
"id" : "post id",
"header" : "Название поста",
"text" : "Содержимое поста"
}

Редактировать посты могу только создатель поста.

### like unlike поста.

Ставить like unlike могут только зарегистрированные пользователи.

по урле  http://127.0.0.1:8000/api/likes/ необходимо отправить post запрос с данными в json формате, пример:

{
"id" : "id поста"
}

в ответ вернется кол-во лайков данного поста.

если user не ставил лайк, то кол-во увеличится на 1, если уже ставил, то уменьшится.






