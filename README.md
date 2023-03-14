![example workflow](https://github.com/antsakharov/foodgram-project-react/actions/workflows/main.yml/badge.svg)
# foodgram-projectt

## Описание проекта: 

•	**Назначение:** 

Foodgram реализован для публикации рецептов. Авторизованные пользователи
могут подписываться на понравившихся авторов, добавлять рецепты в избранное,
в покупки, скачать список покупок ингредиентов для добавленных в покупки
рецептов.

•	**Реализованный функционал:** 

- делитесь своими рецептами
- смотрите рецепты других пользователей
- добавляйте рецепты в избранное
- быстро формируйте список покупок, добавляя рецепт в корзину
- следите за своими друзьями и коллегами

•	**Стек:**

Python, Django, DRF, PostgreSQL, Nginx, Gunicorn, Git, Docker, GitHub Actions, YandexCloud

### Сервис доступен по адресу:
```
http://51.250.12.24/
```
## Инструкция по развёртыванию проекта

### Запуск проекта:
1. Клонируйте проект:
```
git clone https://github.com/antsakharov/foodgram-project-react.git
```
2. Подготовьте сервер:
```
scp docker-compose.yml <username>@<host>:/home/<username>/
scp nginx.conf <username>@<host>:/home/<username>/
scp .env <username>@<host>:/home/<username>/
```
3. Установите docker и docker-compose:
```
sudo apt install docker.io 
sudo apt install docker-compose
```
4. Соберите контейнер и выполните миграции:
```
sudo docker-compose up -d --build
sudo docker-compose exec backend python manage.py migrate
```
5. Создайте суперюзера и соберите статику:
```
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
6. Скопируйте предустановленные данные json:
```
sudo docker-compose exec backend python manage.py loadmodels --path 'recipes/data/ingredients.json'
sudo docker-compose exec backend python manage.py loadmodels --path 'recipes/data/tags.json'
```
7. Данные для проверки работы приложения:
Суперпользователь:
```
email: admin@mail.com
password: admin1234
```
•	**Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env**
```csharp 
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
