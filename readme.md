![logo for git](/images_for_design_project_on_github/logo-for-git.jpg "logo for git") 

## Пед-проект по созданию службы доставки готовой еды на базе фрэймворка Flask.

### Цель:

Создать/написать и оформить веб-приложение предоставляющего возможность пользователю 
заказать готовую еду из иллюстрированного меню на сайте.
В качестве источника вдохновения (готовых блюд) был использован (там действительно вкусно): 
<a href="https://www.edatomsk.ru/">Саша Варит</a>

### Технологии и инструменты:

- Язык программирования: Python версии 3.10;
- Фреймворк Flask версии 3.0.0 с приложениями: 
Flask-Login версии 0.6.3, Flask-Mail версии 0.9.1, 
Flask-Migrate версии 4.0.5, Flask-SQLAlchemy версии 3.1.1, 
Flask-WTF версии 1.2.1;
- СУБД: SQLite;
- Логирование ошибок: Loguru версии 0.7.2;
- Инструменты разработки: IDE PyCharm;
- Версионный контроль: Git;

<details><summary><strong>Структура базы данных (одна не большая картинка):</strong></summary>

#### Корзина покупок реализована в сессии пользователя !

![database_structure](/images_for_design_project_on_github/database_structure.jpg "database_structure") 

</details>

<br>

<details><summary><strong>Структура проекта (одна большая картинка):</strong></summary>

![project_structure](/images_for_design_project_on_github/project_structure.jpg "project_structure") 

</details>

<br>

<details><summary><strong>Пример работы (много больших картинок):</strong></summary>

### index:

![index](/images_for_design_project_on_github/index.jpg "index")

### personal_account:

![personal_account](/images_for_design_project_on_github/personal_account.jpg "personal_account")

### order_history:

![order_history](/images_for_design_project_on_github/order_history.jpg "order_history")

### shopping_cart_user:

![shopping_cart_user](/images_for_design_project_on_github/shopping_cart_user.jpg "shopping_cart_user")

### user_registration:

![user_registration](/images_for_design_project_on_github/user_registration.jpg "user_registration")

### log_in_account:

![log_in_account](/images_for_design_project_on_github/log_in_account.jpg "log_in_account")

### forget_password_enter_email:

![log_in_account](/images_for_design_project_on_github/forget_password_enter_email.jpg "forget_password_enter_email")

### terms_of_delivery:

![terms_delivery](/images_for_design_project_on_github/terms_delivery.jpg "terms_delivery")

### contacts:

![contacts](/images_for_design_project_on_github/contacts.jpg "contacts")

</details>

### Запуск приложения:

1. Скачать архив с медиа файлами формата jpg по ссылке: 
<a href="https://disk.yandex.ru/d/zlikP0QHqR5d3w">медиа файлы (картинки)</a> 
и раcпаковать его содержимое в папку media (находится в корне проекта).
Если этого не сделать то на главной странице отобразиться картинка по умолчанию для 
всех блюд (данная картинка выводится у всех блюд без картинки).
2. Создать файл .env (используется для хранения переменных окружения 
в проекте).
3. Формат файла .env:

SECRET_KEY= с генерированный секретный ключ для приложения;

MAIL_SERVER= адрес почтового сервера к которому подключаетесь;

MAIL_PORT= порт почтового сервера к которому подключаетесь;

MAIL_USE_TLS= True или Fals (в зависимости от конфигураций сервера);

MAIL_USERNAME= адрес электронной почты;

MAIL_DEFAULT_SENDER= еще раз адрес электронной почты;

MAIL_PASSWORD= пароль для подключения к почтовому серверу;

4. Установить все зависимости/библиотеки указанные в requirements.txt.
5. Инициализируйте и заполните базу данных по средствам следующих команд 
(соглано приведенному ниже порядку) в командной строке (в дирректории проекта):

flask init-db

flask add-categories_meal-in-db

flask add-meal-in-db

База данных заполняется на основе содержания файла фикстур categories_meal.json 
и meal.json расположенных в папке fixtures .

Так же архив с файлом базы данных можно скачать 
<a href="https://disk.yandex.ru/d/LZx_ORzc2kGu3w">по ссылке (база данных)</a>.

6. Запустить выполнение файла wsgi.py.