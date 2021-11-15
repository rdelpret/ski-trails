FROM python:latest
WORKDIR /app
ADD . . 
RUN pip3 install -r requirements.txt
