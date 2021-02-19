ARG REPO=python
ARG TAG=3.8-alpine

FROM ${REPO}:${TAG}

WORKDIR /home

COPY ./requirements.txt .
COPY ./configuration.yaml .
COPY ./id.py .
COPY ./main.py .
COPY ./mqtt.py .
COPY ./webserver.py .

RUN python3 -m pip install --upgrade pip \
&&  python3 -m pip install -r /home/requirements.txt \
&&  rm /home/requirements.txt

ENTRYPOINT python3 /home/main.py