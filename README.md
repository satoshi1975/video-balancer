# Video Traffic Load Balancer

### Установка и запуск

1. Склонируйте репозиторий:
    ```bash
    git clone <repository_url>
    ```

2. Запустите сервис с помощью Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. Примените миграции базы данных:
    ```bash
    docker-compose exec web alembic upgrade head
    ```

4. Сервис будет доступен по адресу:
    ```
    http://localhost:8000
    ```

### API

#### 1. Редирект видео

    ```
    GET / Параметр: video (URL видео)
    ```


#### 2. Конфигурация

- Получить конфигурацию:
    ```
    GET /config
    ```

- Обновить конфигурацию:
    ```
    PUT /config
    Параметры: cdn_host (string), ratio (integer)
    ```
