# - ARG define arguments
# - FROM define aliases
# - RUN to execute commands

ARG PYTHON_VERSION=3.9-slim-bullseye

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

# - Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
   build-essential \
   libpq-dev 

# -Copy content from requirements folder
COPY ./requirements .
