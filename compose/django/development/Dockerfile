FROM python:3.5

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add requirements
COPY ./requirements /requirements

# Install dependencies.
RUN pip install -r /requirements/local.txt

# Set work directory.
WORKDIR /src
COPY . /src

# Copy files.
COPY ./compose/django/development/start.sh /start.sh
COPY ./compose/django/entrypoint.sh /entrypoint.sh

# Run migrations and test db.
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /start.sh \
    && chmod +x /entrypoint.sh \
    && chmod +x /start.sh

ENTRYPOINT ["/entrypoint.sh"]
