# Тестовое задание - проект Вопрос-ответ

Проект является тестовым заданием по написанию API

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.0.2-green)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.14.0-red)](https://www.django-rest-framework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-✓-blue)](https://www.postgresql.org)
[![Pytest](https://img.shields.io/badge/Pytest-7.4.4-yellow)](https://pytest.org)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-21.2.0-darkgreen)](https://gunicorn.org)

## 🚀 Методы API:
## 1.	Вопросы (Questions):
○	GET /questions/ — список всех вопросов 
○	POST /questions/ — создать новый вопрос
○	GET /questions/{id} — получить вопрос и все ответы на него
○	DELETE /questions/{id} — удалить вопрос (вместе с ответами)

## 2.	Ответы (Answers):
○	POST /questions/{id}/answers/ — добавить ответ к вопросу
○	GET /answers/{id} — получить конкретный ответ
○	DELETE /answers/{id} — удалить ответ


## 📦 Установка и запуск
Клонируем репозиторий из GitHub
Запускаем проект при помощи Docker командой 
```cmd
docker-compose up --build   
```
Также отдельно можно запустить тестирование командой
```cmd
docker-compose run --rm tests
```

### Клонирование репозитория

```bash
git clone https://github.com/Alexsandr007/question_project.git
cd .\question_project\       