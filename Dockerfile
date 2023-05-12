FROM ubuntu:20.04

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         python3-pip \
         python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app

RUN pip3 install --trusted-host pypi.python.org tensorflow flask pillow

COPY . /app

ENTRYPOINT ["python", "inference.py"]
