FROM python:3.9-slim-buster

RUN pip install --upgrade pip 

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]