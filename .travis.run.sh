#!/bin/bash

cp .env.example .env

python manage.py migrate

pytest --cov=boards --cov=accounts  --ds=myproject.settings

coveralls

codecov