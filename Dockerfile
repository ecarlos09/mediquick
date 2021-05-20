FROM python:3.8.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code/
# CMD [ "python3", "-m" , "Django", "run", "--host=127.0.0.1"]
# CMD ["python", "-m",  "django", ./mediquick/manage.py", "runserver", "--host=127.0.0.1" ]