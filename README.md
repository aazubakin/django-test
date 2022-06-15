## Тестовое задание на позицию Backend Python

### Необходимо реализовать приложение Django.

#### Описание:

В листе organization список компаний клиента (client_name + name уникально).

bills.xlsx - это список счетов организации клиента. Уникальность по полям client_org и №.

Необходимо реализовать загрузку этих файлов через форму и заполнить БД (SQLite или PostgreSQL) находящимися записями. Условие уникальности записей должно сохраняться и в БД.

#### Это должно быть приложение Django состоящее из:

1. страница с формами загрузки файлов (можно разные страницы)
2. страница со списком клиентов колонки: Название, Кол-во организаций, Приход (сумма по счетам всех организаций клиента)
3. страница со списком счетов с фильтром по организации или по клиенту.
4. В этом же приложении реализовать api (используя DRF), эндпоинт загрузки файлов bills.xlsx и client_org.xlsx (может быть по одному на файл, как посчитаете правильным)
5. эндпоинт со списком счетов с возможностью фильтровать по организации или по клиенту

### Как запустить приложение?

1. На одном уровне с папкой webapp создаем папку postgresql-db с файлом: .pg-env:

\*adjust names and passwords to your real passwords and names

POSTGRES_USER=deploy-test-user
POSTGRES_PASSWORD=your-deploy-test-password
POSTGRES_DB=deploy-db

2. Создайте файл locals_vars.py in webapp/src/project/ и не забудьте добавить в .gitignore:

SECRET_KEY = 'django-insecure-wa#75l@ub0+vr1_q^(34nvew(-6$v&lk^vhgbxj5#1z7+q+%65'
PG_NAME = 'deploy-db' # as a POSTGRES_DB in .pg-env
PG_USER = 'deploy-test-user' # as in POSTGRES_USER in .pg-env
PG_PASSWORD = 'your-deploy-test-password' # as a POSTGRES_PASSWORD in .pg-env
PG_HOST = 'postgresql-db' # as the DB's service name in docker-compose.yml

3. Далее меняем настройки в settings.py,

from . import locals_vars # should in .gitignore

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': locals_vars.PG_NAME,
'USER': locals_vars.PG_USER,
'PASSWORD': locals_vars.PG_PASSWORD,
'HOST': locals_vars.PG_HOST,
'PORT': '', # default
}
}

4. docker-compose up --build

5. Выполнить миграции:

docker-compose exec webapp bash
cd src/
python manage.py migrate
