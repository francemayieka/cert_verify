#!/bin/bash
/usr/local/bin/pip install -r requirements.txt
/usr/local/bin/python manage.py collectstatic --noinput
