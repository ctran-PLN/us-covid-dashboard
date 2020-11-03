FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /my_app_dir

ADD requirements.txt /my_app_dir/

RUN pip install -r requirements.txt

ADD . /my_app_dir/

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait
