# Используем официальное изображение Python
FROM python:3.12-slim

# Устанавливаем переменную окружения для Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Pillow
RUN pip install gunicorn

# Копируем все файлы проекта в контейнер
COPY . /app/

# Указываем STATIC_ROOT
ENV DJANGO_STATIC_ROOT=/app/staticfiles

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Открываем порт 8000
EXPOSE 8010

# Команда для запуска Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]
# Запустите Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8010", "mydjangoprj.wsgi:application"]