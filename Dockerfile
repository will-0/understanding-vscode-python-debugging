FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

WORKDIR /app

# Install requirements
COPY ./src/requirements.txt /tmp/pip-tmp/

RUN pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

COPY ./src /app

CMD ["python", "main.py"]