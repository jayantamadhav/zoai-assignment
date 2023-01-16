FROM python:3.10

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip wheel setuptools 
RUN pip install -r ./requirements.txt
CMD uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000