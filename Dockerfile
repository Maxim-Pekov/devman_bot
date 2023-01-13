FROM ubuntu:latest
MAINTAINER Maxim Pekov 'Max.Pekov@gmail.com'
RUN apt-get update -qy
RUN apt-get install -qy python3.10 python3-pip python3.10-dev
COPY . /bot
WORKDIR /bot
RUN pip install -r requirements.txt
CMD ["python3","main.py"]