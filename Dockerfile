FROM python:3.14

ADD requirements.txt /tmp
RUN ["pip3", "install", "-r", "/tmp/requirements.txt"]

EXPOSE 8000