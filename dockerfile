FROM docker.artifactory.gmfinancial.com/python:3.10-alpine
LABEL maintainer="GM Financial"

ENV AZDO_CLIENT_SECRET=${AZDO_CLIENT_SECRET} \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

RUN mkdir /app
WORKDIR /app

COPY src/ requirements.txt /app/

RUN apk update && \
    apk upgrade --available && sync && \
    pip install --upgrade --index-url https://artifactory.gmfinancial.com/artifactory/api/pypi/virtual-pypi/simple pip && \
    pip install -r requirements.txt --index-url https://artifactory.gmfinancial.com/artifactory/api/pypi/virtual-pypi/simple pip setuptools && \
    adduser -D -g teamsbot teamsbot teamsbot && \
    chown -R teamsbot:teamsbot /app

USER teamsbot

EXPOSE 3978

ENTRYPOINT [ "python3","/app/main.py" ]