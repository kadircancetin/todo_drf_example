FROM python:3.8.3-slim-buster

LABEL maintainer="kadircancetin@gmail.com"

ENV PYTHONUNBUFFERED=1 \
 PYTHONDONTWRITEBYTECODE=1 \
 # pip:
 PIP_NO_CACHE_DIR=off \
 PIP_DISABLE_PIP_VERSION_CHECK=on \
 PIP_DEFAULT_TIMEOUT=100 \
 # poetry:
 POETRY_VERSION=1.1.4 \
 POETRY_VIRTUALENVS_CREATE=false \
 POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# System deps:
RUN pip install "poetry==$POETRY_VERSION" && poetry --version

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml ./app/

# Project initialization:
RUN cd /app && poetry install --no-interaction --no-ansi

WORKDIR /app
