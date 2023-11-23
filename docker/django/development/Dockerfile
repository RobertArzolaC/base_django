FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set work directory.
COPY . /src
WORKDIR /src

# Install dependencies.
RUN pip install --upgrade pip
RUN pip install -r ./requirements/development.txt
RUN pip install -r ./requirements/linters.txt

# Copy files.
COPY ./docker/django/development/start.sh /start.sh

# Run migrations and test db.
RUN sed -i 's/\r//' /start.sh && chmod +x /start.sh

# Run start.sh.
CMD ["/start.sh"]
