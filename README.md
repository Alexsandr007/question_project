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
○	GET /questions/ — список всех вопросов <br>
○	POST /questions/ — создать новый вопрос <br>
○	GET /questions/{id} — получить вопрос и все ответы на него <br>
○	DELETE /questions/{id} — удалить вопрос (вместе с ответами) <br>

## 2.	Ответы (Answers):
○	POST /questions/{id}/answers/ — добавить ответ к вопросу <br>
○	GET /answers/{id} — получить конкретный ответ <br>
○	DELETE /answers/{id} — удалить ответ


## 📦 Установка и запуск
Клонируем репозиторий из GitHub
Запускаем проект при помощи Docker командами при первом запуске
```cmd
docker-compose build --no-cache   
docker-compose up                 
```
При вторичном и дальнейших запусках можно использовать более удобную команду
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
```
### Переход в корневую директорию проекта
```cmd
cd .\question_project\  
```     