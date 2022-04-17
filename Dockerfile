FROM python:3.7-alpine
RUN apk update
RUN apk add git
WORKDIR .
COPY . .
RUN pip install -r Azalea/requirements.txt