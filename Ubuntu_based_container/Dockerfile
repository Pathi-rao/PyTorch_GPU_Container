# defines how our Docker image looks like

#create a ubuntu base by pulling it from dockerhub
# FROM ubuntu:20.04
FROM nvidia/cuda:11.6.1-cudnn8-runtime-ubuntu20.04
# set the conda path in the path variables
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"


# install necessary packages(we'll do the dependencies later)
RUN apt-get update \
    && apt install -y python3-dev wget

# install mini conda inside the container and remove the file when done
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh \
    && mkdir root/.conda\
    && sh Miniconda3-py39_4.11.0-Linux-x86_64.sh -b \
    && rm -f Miniconda3-py39_4.11.0-Linux-x86_64.sh

# create a new conda env
RUN conda create -y -n siamese_conda_env python=3.9
# siamese_conda_env is the name of the conda env

# copy our entire code from local machine to a src folder in container
COPY . src/


RUN /bin/bash -c "cd src \
    && source activate siamese_conda_env \
    && pip install -r requirements.txt"