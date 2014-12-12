FROM debian:wheezy
RUN apt-get update && apt-get install -y python python-pip python-dev libpq-dev postgresql-client gettext

# Using PIL or Pillow? You probably want to uncomment next line
# RUN apt-get update && apt-get install -y libjpeg8-dev

ADD . /app
WORKDIR /app

RUN ./bin/peep.py install -r requirements.txt

EXPOSE 80

CMD ["./bin/run-docker.sh"]
