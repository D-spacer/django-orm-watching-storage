# Пульт охраны банка
Данный скрипт предназначен для сотрудников безопасности банка. Если у вас нет доступа к базе данных, вы не сможете его запустить, но его можно адаптировать для собственных нужд, если вы подключите собственную базу данных.
Скрипт запускает сайт, на котором можно просматривать информацию по активным пропускам к хранилищу, просматривать посещения хранилища каждым сотркдником и отслеживать подозрительные посещения, если сотрудник находился в хранилище слишком долго.

## Как установить
Для установки необходимо скачать данный скрипт. Перед запуском необходимо создать файл .env, в котором будут храниться данные для доступа к базе данных.
В файле следует указать следующие данные:
1. DB_HOST - имя хоста для подключения к БД
2. DB_PORT - порт для подключения к БД
3. DB_NAME - имя базы данных
4. DB_USER - имя пользователя/администратора для подключения к базе
5. DB_PASSWORD - пароль к базе данных
7. DEBUG - режим отладки сайта (значение True или False)
8. ALLOWED_HOSTS - список хостов, с которыми будет работать сайт. Оформляется как [<хост_1>, <хост_2>...]

Сайт запускается с помощью команды

```python manage.py runserver 0.0.0.0:8000```

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```pip install -r requirements.txt```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
