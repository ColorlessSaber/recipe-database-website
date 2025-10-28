FROM python:3.13.9-slim

# Prevents Django from writing .pyc files inside the container
ENV PYTHONDONTWRITEBYECODE=1

# Sends locks to the container console without buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000