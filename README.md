# Blogicum
Блокикум - социальная сеть для публикации личных дневников.
Сайт, на котором пользователь может создать свою страницу и публиковать на ней сообщения («посты»), которые могут относиться к определённым категориям.
Пользователь может перейти на страницу любой категории и увидеть все посты, которые к ней относятся.
![image](https://github.com/user-attachments/assets/6280090d-2c2f-4bf6-9d9e-77ad582c7e59)

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/kdmitrykk/Blogicum
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd hotelservice
    ```

3. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv env
    ```

    ```bash
    .\env\Scripts\activate  # Windows
    source env/bin/activate  # macOS и Linux
    ```

4. Обновите pip:
    ```bash
    python -m pip install --upgrade pip
    ```

5. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

6. Выполните миграции базы данных:
    ```sh
    python manage.py migrate
    ```

7. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

# Используемые технологии

* Python
* Django
* HTML, CSS

# Автор
Крикунов Дмитрий
