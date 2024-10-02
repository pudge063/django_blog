#!/bin/sh

# Ожидаем подключения к базе данных
while ! nc -z $DB_HOST $DB_PORT; do
  echo "Waiting for the database..."
  sleep 1
done

# Применяем миграции
python manage.py migrate

# Собираем статические файлы
python manage.py collectstatic --noinput

# Запускаем Gunicorn
exec "$@"
