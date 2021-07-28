FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN pip3 install django
RUN pip3 install djangorestframework
RUN pip3 install django-filter

RUN mkdir /code
WORKDIR /code
COPY . /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt



