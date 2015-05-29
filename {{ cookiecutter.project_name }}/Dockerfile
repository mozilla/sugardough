FROM python:3-slim

EXPOSE 8000
CMD ["./bin/run-prod.sh"]

RUN adduser --uid 1000 --disabled-password --gecos '' webdev && \
    chown -R webdev:webdev /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential python-dev libpq-dev postgresql-client gettext && \
    rm -rf /var/lib/apt/lists/*

# Using PIL or Pillow? You probably want to uncomment next line
# RUN apt-get update && apt-get install -y --no-install-recommends libjpeg8-dev

WORKDIR /app

# First copy requirements.txt and peep so we can take advantage of
# docker caching.
COPY ./bin/peep.py /app/bin/peep.py
COPY requirements.txt /app/requirements.txt
RUN ./bin/peep.py install -r requirements.txt

USER webdev
COPY . /app
RUN DEBUG=False SECRET_KEY=foo ALLOWED_HOSTS=localhost, DATABASE_URL= ./manage.py collectstatic --noinput -c
