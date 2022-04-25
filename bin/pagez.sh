#!/usr/bin/env bash

pip install -r requirements.txt

cd src

python3 manage.py runserver 0.0.0.0:8000