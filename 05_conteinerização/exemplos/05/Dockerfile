FROM python:3.10-alpine

RUN mkdir -p /app 

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD flask --app app run --host 0.0.0.0