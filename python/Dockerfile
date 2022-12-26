FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \ 
&& apt-get -y install gcc libpq-dev 

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
