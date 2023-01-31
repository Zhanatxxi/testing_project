#!/bin/sh

port=8000
workers=4

alembic upgrade head

cd ../ && uvicorn main:app --host 0.0.0.0 --workers "$workers" --port "$port"