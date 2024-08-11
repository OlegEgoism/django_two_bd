Django проект демонстрирует, как настроить и использовать несколько баз данных PostgreSQL в одном Django приложении. 
Проект включает в себя настройку двух отдельных баз данных, каждая из которых связана с разными моделями Django.
Пользовательский маршрутизатор баз данных направляет запросы к правильной базе данных: db_router.py


Проект содержит два основных приложения Django:
- one: Содержит модели и представления, связанные с первой базой данных (os1).
- two: Содержит модели и представления, связанные со второй базой данных (os2).


Создайте:
- python manage.py makemigrations one
- python manage.py makemigrations two
- python manage.py migrate --database=os1
- python manage.py migrate --database=os2

Проверьте статус миграций:
- python manage.py showmigrations