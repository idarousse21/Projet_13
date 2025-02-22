FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PORT=8000
CMD python manage.py runserver 0.0.0.0:$PORT