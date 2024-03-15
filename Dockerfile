FROM ubuntu

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-pandas \
    python3-numpy \
    python3-seaborn \
    python3-matplotlib \
    python3-scikit-learn \
    python3-scipy


RUN mkdir -p /home/doc-bd-a1/

# Set working directory
WORKDIR /home/doc-bd-a1/
