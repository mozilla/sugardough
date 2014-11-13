FROM debian
RUN apt-get update && apt-get install -y python python-pip python-dev libpq-dev mysql-client libmysqlclient-dev

ADD . /app
WORKDIR /app

RUN ./bin/peep.py install -r requirements/base.txt
RUN ./bin/peep.py install -r requirements/dev.txt

EXPOSE 80

CMD ["./bin/run-docker.sh"]
