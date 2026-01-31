FROM python:3.9

WORKDIR /app/registration_system

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
