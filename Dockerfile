FROM python:3.11

WORKDIR /
COPY requirements.txt /
COPY src/ /
COPY .env /

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 4003

CMD [ "--host", "0.0.0.0", "--port", "4003", "--env-file", ".env" ]
ENTRYPOINT [ "uvicorn" , "services:app"]
