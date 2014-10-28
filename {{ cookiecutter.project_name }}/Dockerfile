FROM debian
RUN apt-get update && apt-get install -y python python-pip python-dev mysql-client libmysqlclient-dev
RUN pip install peep

ADD . /app
WORKDIR /app

RUN peep install -r requirements/base.txt
RUN peep install -r requirements/dev.txt
