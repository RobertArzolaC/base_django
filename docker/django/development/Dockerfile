FROM python:3.5

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set work directory.
COPY . /src
WORKDIR /src

# Install dependencies.
RUN pip install --upgrade pip
RUN pip install -r ./requirements/development.txt

# Copy files.
COPY ./docker/django/development/start.sh /start.sh
COPY ./docker/django/entrypoint.sh /entrypoint.sh

# Run migrations and test db.
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /start.sh \
    && chmod +x /entrypoint.sh \
    && chmod +x /start.sh

ENTRYPOINT ["/entrypoint.sh"]
