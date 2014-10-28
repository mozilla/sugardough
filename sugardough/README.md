sugardough
==========


Docker for development
----------------------

0. Make sure you have [docker](https://docker.io) and [pip](https://pypi.python.org/pypi/pip/1.5.6)
1. fig up

Note that this will probably not work with
[boot2docker](https://github.com/boot2docker/boot2docker), as the
volumes will not get mounted.


Docker for deploying to production
-----------------------------------

1. Add your project in [Docker Registry](https://registry.hub.docker.com/) as [Automated Build](http://docs.docker.com/docker-hub/builds/)
2. Prepare a 'env' file with all the varibles needed by dev, stage or production.
3. Run the image:

    docker run --env-file env -p 80:80 mozilla/sugardough
