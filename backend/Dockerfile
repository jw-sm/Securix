FROM python:3.13-slim-bookworm

WORKDIR /backend

# Avoid making .pyc files to reduce clutter in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Unbuffered output, so logs appear immediately
ENV PYTHONBUFFERED 1

# install system dependencies
# updates the package index
RUN apt-get update \
    && apt-get -y install netcat-openbsd gcc postgresql \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install python dependencies
RUN pip install --upgrade pip
# copy requirements from local to container
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the local "backend" folder into the container
COPY . /backend
