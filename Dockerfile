FROM python:3.10-slim-buster

RUN pip install --upgrade pip 

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

EXPOSE 4000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]