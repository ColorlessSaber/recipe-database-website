## Stage 1 - Build Stage
# Use an offical Docker Python runtime image
FROM python:3.13-slim AS builder

# create the app directory and set the working directory inside the container
RUN mkdir /app
WORKDIR /app

# Prevents Django from writing .pyc files inside the container
ENV PYTHONDONTWRITEBYECODE=1
# Sends locks to the container console without buffering
ENV PYTHONUNBUFFERED=1

# install the ncessary libraries
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

## Stage 2 - Production Stage
FROM python:3.13-slim

# Create a non-root user for the container, create app directory, and set the appuser to the /app
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

# Copy the python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Create the working directory and copy application code over
WORKDIR /app
COPY --chown=appuser:appuser . .

# Prevents Django from writing .pyc files inside the container
ENV PYTHONDONTWRITEBYECODE=1
# Sends locks to the container console without buffering
ENV PYTHONUNBUFFERED=1

# switch to non-root user
USER appuser

# Expose the Django port
EXPOSE 8000