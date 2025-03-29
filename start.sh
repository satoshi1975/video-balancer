#!/bin/bash

set -e

echo "Running migrations..."
alembic upgrade head || { echo 'Migration failed, exiting.'; exit 1; }

echo "Migrations done, starting application..."

# Эта команда должна запускать сервер Uvicorn и блокировать завершение контейнера
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
