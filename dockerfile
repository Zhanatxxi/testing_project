FROM python:3.10.9-alpine3.17

WORKDIR /app

COPY . /app

COPY ./requirements.txt /app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN chmod +x /app/docker-entrypoint.sh

CMD [ "uvicorn", "main:app", "--host" ,"0.0.0.0", "--port", "8000"] 

EXPOSE 8000
