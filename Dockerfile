FROM ubuntu:22.04

RUN rm -rf /root/.gnupg /root/.npm /tmp/* /var/lib/lists/* /var/libs/dpkg/*-old /usr/local/lib/node_modules /var/cache/* /var/log/*

WORKDIR /app

RUN apt-get -qq update \
    && apt-get -qq install --yes --no-install-recommends python3 python3-pip gdal-bin cmake pdal libpdal-plugin-e57 \
    && rm -rf /var/cache/* /var/log/* /var/lib/apt/lists/* /var/lib/dpkg/*-old

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
