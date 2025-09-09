FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирование проекта
COPY . .

# Сбор статических файлов
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "question_project.wsgi:application", "--bind", "0.0.0.0:8000"]