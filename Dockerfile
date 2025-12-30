FROM python:3.14

EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ADD requirements.txt /tmp
RUN ["pip3", "install", "-r", "/tmp/requirements.txt"]

ADD journal /journal

WORKDIR /journal

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]