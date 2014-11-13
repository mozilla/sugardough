FROM debian
RUN apt-get update && apt-get install -y python python-pip python-dev libpq-dev mysql-client libmysqlclient-dev

ADD . /app
WORKDIR /app

RUN ./bin/peep.py install -r requirements/base.txt
RUN ./bin/peep.py install -r requirements/dev.txt

RUN ./manage.py collectstatic --noinput -c

EXPOSE 80

CMD ["gunicorn", "sugardough.wsgi:application", "-b 0.0.0.0:80", "-w 2", "--log-file", "-"]
