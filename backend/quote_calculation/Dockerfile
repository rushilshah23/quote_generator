FROM python:3.12.6-alpine

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN "pip install -r requirements.txt"

COPY . .

CMD [ "python","" ]



