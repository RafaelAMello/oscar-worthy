FROM python:3.6

COPY requirements.txt /app/
WORKDIR /app
RUN python -m pip install -r requirements.txt
