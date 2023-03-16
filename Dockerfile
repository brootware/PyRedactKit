FROM python:3.10-alpine

WORKDIR /workdir

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade pyredactkit

ENTRYPOINT ["/usr/local/bin/prk"]