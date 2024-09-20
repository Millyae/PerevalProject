# PerevalProject
Проект Pereval предназначен для управления перевалами и их данными.

# Установка

1. Склонируйте репозиторий:
   ```bash
   git clone <https://github.com/Millyae/PerevalProject>
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd PerevalProject
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Настройте переменные окружения в файле `.env`:
   ```plaintext
   DB_NAME=pereval
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

# Запуск проекта

Запустите сервер разработки:
```bash
python manage.py runserver
```

Проект будет доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

# Документация API

Документация API будет доступна по адресу [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/).

# Методы API

## **GET /submitData/<id>**

- **Описание**: Получение информации о перевале по его ID.
- **Параметры**:
  - `id` — ID перевала.
- **Ответ**:
  ```json
  {
      "date_added": "2023-09-20T12:00:00Z",
      "beauty_title": "Beautiful Pereval",
      "title": "Test Pereval",
      "other_titles": null,
      "connect": null,
      "add_time": "2023-09-20T12:00:00Z",
      "coord": {
          "latitude": 50.0,
          "longitude": 60.0,
          "height": 1000
      },
      "level_winter": null,
      "level_summer": null,
      "level_autumn": null,
      "level_spring": null,
      "status": "new"
  }
  ```

## **PATCH /submitData/<id>**

- **Описание**: Обновление существующего перевала, если статус "new".
- **Параметры**:
  - `id` — ID перевала.
  - JSON с обновляемыми полями (все поля, кроме ФИО и адреса электронной почты):
    ```json
    {
        "title": "Updated Title",
        "beauty_title": "Updated Beauty Title",
        ...
    }
    ```
- **Ответ**:
  ```json
  {
      "state": 1,
      "message": "Record updated successfully"
  }
  ```

## **GET /submitData/?user__email=<email>**

- **Описание**: Получение всех перевалов, отправленные пользователем с указанным адресом почты.
- **Параметры**:
  - `user__email` — адрес электронной почты пользователя.
- **Ответ**:
  ```json
  [
      {
          "date_added": "2023-09-20T12:00:00Z",
          "title": "Test Pereval",
          ...
      },
      ...
  ]
  ```

## Тесты

Запустите тесты с помощью команды:
```bash
python manage.py test
```
