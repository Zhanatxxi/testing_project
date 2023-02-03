#!/bin/sh

port=8000
workers=4


alembic upgrade head

python main.py
