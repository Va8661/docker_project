FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y build-essential && \
    pip install --upgrade pip && \
    pip install uwsgi && \
    pip install uwsgi-tools


COPY . /code/

RUN mkdir /run/uwsgi
RUN chown www-data:www-data /run/uwsgi/ && chmod 777 /run/uwsgi/

EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]

