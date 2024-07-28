#!/bin/bash

# Use the virtual environment provided by Vercel
source /vercel/path0/venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
