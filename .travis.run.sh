#!/bin/bash

cp .env.example .env

python manage.py migrate

pytest --ds=myproject.settings