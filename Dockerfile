FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE geo_data_project.settings

# Открываем порт 8000
EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
