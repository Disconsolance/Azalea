FROM python:3.7-alpine
RUN apk update
RUN apk add git
WORKDIR ./Azalea
RUN pip install -r requirements.txt
CMD ["python", "main.py"]