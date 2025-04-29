FROM python:3.12-alpine

COPY requirements.txt requirements.txt

RUN apk add --no-cache --virtual .build-deps build-base && \
    pip3 install --no-cache-dir --upgrade pip pip-tools  && \
    pip-sync --python-executable python3 \
    --pip-args "--disable-pip-version-check --root-user-action=ignore --no-cache-dir" && \
    apk del --no-cache .build-deps
