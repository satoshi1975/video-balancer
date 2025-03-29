FROM python:3.9

WORKDIR /app

# Копируем только requirements.txt сначала для кэширования
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы (кроме указанных в .dockerignore)
COPY ./app ./app
COPY ./start.sh .
COPY ./migrations ./migrations

# Делаем скрипт исполняемым
RUN chmod +x /app/start.sh

# Указываем рабочую директорию для volume
WORKDIR /app/app