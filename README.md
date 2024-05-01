# Установка, настройка и использование веб-приложения

## Шаг 1: Скачать код с репозитория
```
git clone https://github.com/nuray0/executive_test_project.git
```

## Шаг 2: Перейти в папку проекта
```
cd executive_test_project
```

## Шаг 3: Установите Docker
Если вы еще не установили Docker, скачайте и установите его с [официального сайта Docker.](doc:[linking-to-pages#anchor-links](https://www.docker.com/get-started))

## Шаг 4: Запустите Docker Desktop
Чтобы убедиться, что Docker работает, откройте терминал (или командную строку на Windows) и выполните команду ```docker --version```. Если Docker установлен правильно, вы увидите версию Docker, установленную на вашем компьютере


## Шаг 3: Создать миграции
```
docker-compose run web python manage.py makemigrations
```

## Шаг 4: Применить миграции
```
docker-compose run web python manage.py migrate
```

## Шаг 5: Запустить контейнеры Docker
```
docker-compose up
```

## Шаг 6: Как запустился Docker, открыть приложение в браузере по адресу
```
http://0.0.0.0:8000/
```

Если по этому адресу выше не открывается, попробуйте зайти по:
```
http://localhost:8000/
```
или
```
http://127.0.0.1:8000/
```

## Шаг 7: Создать аккаунт и войти
![Страница для регистрации](https://github.com/nuray0/executive_test_project/raw/master/assets/images/signup_page.jpeg)
![Страница для входа](https://github.com/nuray0/executive_test_project/raw/master/assets/images/login_page.jpeg)

## Шаг 8: Создать управляющего
![Главная страница](https://github.com/nuray0/executive_test_project/raw/master/assets/images/dashboard_empty.jpeg)
![Форма для создания управляющего](https://github.com/nuray0/executive_test_project/raw/master/assets/images/add_executive.jpeg)

## Шаг 9: Добавить больше информации к управляющему (по желанию)
Можно добавить информацию, такую как опыт работы, сертификаты, согласия на занятие должности и образование.
![Главная страница](https://github.com/nuray0/executive_test_project/raw/master/assets/images/executive_details.jpeg)

## Шаг 10: Просмотреть список управляющих
На главной странице отображается список всех управляющих с краткой информацией о каждом из них.
![Главная страница](https://github.com/nuray0/executive_test_project/raw/master/assets/images/dashboard.jpeg)

# Шаг 11: Редактировать и удалять профили управляющих (по желанию)
Вы можете редактировать и удалять управляющих, а также данные их профилей по своему усмотрению.
