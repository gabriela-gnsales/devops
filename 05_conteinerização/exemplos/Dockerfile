FROM python:3.11-alpine

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY falar_feliz_natal.py . 

CMD python /app/falar_feliz_natal.py