FROM python:3-slim

EXPOSE 80

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libpq-dev postgresql-client gettext && \
    apt-get remove mysql-common -y && apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Using PIL or Pillow? You probably want to uncomment next line
# RUN apt-get update && apt-get install -y --no-install-recommends libjpeg8-dev

WORKDIR /app

# First copy requirements.txt and peep so we can take advantage of
# docker caching.
COPY ./bin/peep.py /app/bin/peep.py
COPY requirements.txt /app/requirements.txt
RUN ./bin/peep.py install -r requirements.txt

COPY . /app

CMD ["./bin/run-docker.sh"]
