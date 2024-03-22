#!/bin/bash
# script to set up environment and start flask application

. ~/mimo/bin/activate
. .env
flask run --host=0.0.0.0