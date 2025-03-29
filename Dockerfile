FROM python:3.9

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY ./app ./app
COPY ./start.sh .
COPY ./alembic.ini ./app/alembic.ini
COPY ./migrations ./app/migrations


RUN chmod +x /app/start.sh

WORKDIR /app/app