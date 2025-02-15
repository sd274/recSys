## - This docker file doesn't actually work. There is some non-sence that is needed to get jax and docker playing nice. 

FROM python:3.12-slim


# -- Install poetry
RUN apt-get update \
  && apt-get install -y curl

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.8.0 \
  PATH="/root/.local/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry install

COPY ./app /code/app
COPY run_app.py /code/run_app.py

WORKDIR /code

CMD ["poetry", "run", "python", "run_app.py"]
