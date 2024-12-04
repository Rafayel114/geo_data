# Geo Data Project

##### _API для загрузки данных из файлов Excel и отображения их в различных форматах (JSON, HTML)_


### Установка и запуск

#### 1. Клонирование репозитория

```sh
git clone https://github.com/Rafayel114/geo_data.git
cd geo_data
```

#### 2. Настройка окружения
Создайте файл .env в корневой директории проекта и добавьте в него переменные(по примеру env_example.txt)

#### 3. Запуск контейнеров
```sh
docker-compose up --build
```

Сервис будет доступен на
```sh
http://0.0.0.0:8000/
```


Доступные энпоинты:

- curl -X POST http://0.0.0.0:8000/upload/ \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path_to_your_file/example.xlsx"
- curl -X GET http://0.0.0.0:8000/data/json/
- curl -X GET http://0.0.0.0:8000/data/html/