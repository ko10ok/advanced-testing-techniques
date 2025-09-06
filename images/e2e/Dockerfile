FROM python:3.12-alpine

ARG TARGETPLATFORM

COPY requirements.txt requirements.txt

RUN apk add --no-cache --virtual .build-deps build-base docker-cli curl && \
    pip3 install --no-cache-dir --upgrade pip pip-tools  && \
    pip-sync --python-executable python3 \
    --pip-args "--disable-pip-version-check --root-user-action=ignore --no-cache-dir"

# Install docker-compose based on platform
RUN case "$TARGETPLATFORM" in \
    "linux/amd64") \
        curl -SL https://github.com/docker/compose/releases/download/v2.24.4/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose ;; \
    "linux/arm64") \
        curl -SL https://github.com/docker/compose/releases/download/v2.24.4/docker-compose-linux-aarch64 -o /usr/local/bin/docker-compose ;; \
    *) \
        echo "Unsupported platform: $TARGETPLATFORM" && exit 1 ;; \
    esac && \
    chmod +x /usr/local/bin/docker-compose && \
    docker-compose --version

# Clean up build dependencies after we're done with them
RUN apk del --no-cache .build-deps
