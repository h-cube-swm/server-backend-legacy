FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update 

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y netcat