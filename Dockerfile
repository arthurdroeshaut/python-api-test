FROM ubuntu:20.04

USER root

RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt-get clean

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN useradd -ms /bin/bash user

USER user
WORKDIR /home/user

RUN pip3 install --upgrade pip
COPY ./requirements.txt Requirements/
RUN pip3 install -r Requirements/requirements.txt