FROM python:3.13-slim-bookworm

WORKDIR /backend

# Avoid making .pyc files to reduce clutter in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Unbuffered output, so logs appear immediately
ENV PYTHONBUFFERED 1

# install system dependencies
# updates the package index
RUN apt-get update \
    # netcat: port/server checker
    && apt-get -y install netcat gcc postgresql \
    # Cleans package cache to reduce image size
    && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
# copy requirements from local to container
COPY ./requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

# copy the local "backend" folder into the container
COPY ./backend
