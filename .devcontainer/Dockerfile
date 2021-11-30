# ref: https://github.com/Simbotic/rust-gst-pytorch-gpu/blob/master/.devcontainer/Dockerfile

FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-devel
# FROM creates a layer from the Docker image and we use this image as a base image


USER root
# By default, containers run as root. A container running as root has full control of the host system. 
# As container technology matures, more secure default options may become available. The default user in a 
# Dockerfile is the user of the parent image.

RUN apt-get update
RUN apt-get upgrade -y
# """
# Whenever you run apt-get update in docker container or inside your Dockerfile It creates it's own isolated space 
# which will run all the commands in that particular space without affecting your physical server/environments. Only container
# and your physical server/environments is sharing same kernel. So if you run apt-get update or any other command then it will
# just run in docker container or docker image you are creating.
# """

RUN apt-get install -y software-properties-common
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install libgl1
RUN apt-get install openjdk-8-jdk-headless -qq 
# remeber Jon's lecture about installing jdk...

# Core linux dependencies. 
RUN apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    yasm \
    pkg-config 

RUN python -m pip install --upgrade pip setuptools wheel

# By copying over requirements first, we make sure that Docker will "cache"
# our installed requirements in a dedicated FS layer rather than reinstalling
# them on every build
COPY ./.devcontainer/requirements.txt requirements.txt

# Install the requirements
RUN python -m pip install -r requirements.txt
RUN python -m pip install boto3
RUN python -m pip install pyspark
RUN python -m pip install torchmeta
RUN python -m pip install ipywidgets
RUN python -m pip install mkdocs-material


# if you are using torchmeta, somehow it overrides the torch version
# so, specify it again so that it is compatible with Nvidia 3060Ti GPU or another that uses sm_86
RUN python -m pip install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio==0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

# """

# You have to mount every volume/hardware to docker you want to use. 
# its really encapsulating the whole system 
# e.g. if you want to use you webcam via usb in a docker container you would have to specify something like:

#     devices:

#     /dev/ttyUSB0:/dev/ttyUSB0
# """

# Only needed for Jupyter
EXPOSE 8888

WORKDIR /src/notebooks

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
# What is Tini and why to use it? ref: https://github.com/krallin/tini/issues/8
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

# Diff b/w ENTRYPOINT and CMD: https://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
