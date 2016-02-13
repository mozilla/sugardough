#!/bin/bash
docker rm -f $(sed s/_//g <<< jenkins${JOB_NAME}${BUILD_NUMBER})_db_1
