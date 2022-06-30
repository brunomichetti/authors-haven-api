# - ARG define arguments
# - FROM define aliases
# - RUN to execute commands
# - ENV define env variables
# - Char "\" used for new lines

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


# -run wheel (required for pypi)
RUN pip wheel --wheel-dir /usr/src/app/wheels \
   -r ${BUILD_ENVIRONMENT}.txt

# - alias for python
FROM python as python-run-stage

# - Define args for build environment and app folder
ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

# - Don't allow Python to write .py files to disk
ENV PYTHONDONTWRITEBYTECODE 1

# - Python output is transmitted to the terminal
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# - Install the required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*


# - Copy the python dependencies wheels
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# - Use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
   && rm -rf /wheels/

# - Run entrypoint script to connect the db service
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


# - Run script for migration and to run the server
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# - Copy the application to the app directory
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
