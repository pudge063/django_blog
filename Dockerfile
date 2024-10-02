# Используем Python 3.10 как базовый образ
FROM python:3.10

RUN apt-get update && apt-get install -y netcat-openbsd

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Копируем файл entrypoint.sh и делаем его исполняемым
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Открываем порт 8000
EXPOSE 8000

# Указываем entrypoint
ENTRYPOINT ["/entrypoint.sh"]

WORKDIR /app/pivnuha

# Команда для запуска Gunicorn
CMD ["gunicorn", "pivnuha.wsgi:application", "--bind", "0.0.0.0:8000"]
