FROM python:3.12-alpine as base

WORKDIR /app

# Install system dependencies
RUN apk add --no-cache curl

# Install Python dependencies
ADD requirements.txt .
RUN python3 -m pip install -r requirements.txt

# Add application files
ADD serve.py .
ADD migrations.py .

FROM base as service
CMD ["python3", "serve.py"]

FROM base as migrations
CMD ["python3", "migrations.py"]
