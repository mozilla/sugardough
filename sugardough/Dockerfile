FROM debian:wheezy
RUN apt-get update && apt-get install -y python python-pip python-dev libpq-dev postgresql-client gettext

# Using PIL or Pillow? You probably want to uncomment next line
# RUN apt-get update && apt-get install -y libjpeg8-dev

WORKDIR /app

# First copy requirements.txt and peep so we can take advantage of
# docker caching.
COPY requirements.txt /app/requirements.txt
COPY ./bin/peep.py /app/bin/peep.py
RUN ./bin/peep.py install -r requirements.txt

COPY . /app

EXPOSE 80

CMD ["./bin/run-docker.sh"]
