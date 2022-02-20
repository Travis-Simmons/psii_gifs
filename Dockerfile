FROM ubuntu:18.04

WORKDIR /opt
COPY . /opt

USER root

ENV IRODS_USER=anonymous

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    gcc \
    gnupg \
    wget 


RUN apt-get update
RUN apt-get install -y python3.6-dev \
                       python3-pip \
                       wget \
                       build-essential \
                       software-properties-common \
                       apt-utils \
                       ffmpeg \
                       libsm6 \
                       libxext6

RUN apt-get update
RUN apt-get install -y libgdal-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN ldconfig
RUN apt-get install -y locales && locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'
# RUN docker pull irods/icommands:4.0.3
# RUN docker run -ti irods/icommands:4.0.3

ENTRYPOINT [ "/usr/bin/python3", "/opt/notebooks/psii_conversion.py" ]

