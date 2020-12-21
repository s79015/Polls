FROM python:3.8.1

ENV PYTHONUNBUFFERED=1

WORKDIR /mysite

ADD . /mysite


RUN pip install -r requirements.txt

# RUN python manage.py migrate

# RUN apt-get update && apt-get install -y
# gcc
# gettext
# # mysql-client default-libmysqlclient-dev
# # postgresql-client libpq-dev
# sqlite3
# # –no-install-recommends && rm -rf /var/lib/apt/lists/*

# EXPOSE 8000

# CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
# CMD uwsgi --module=myapp.wsgi --http=0.0.0.0:8000

# FROM python:3
# ENV PYTHONUNBUFFERED=1
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/