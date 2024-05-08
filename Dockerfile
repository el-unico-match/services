FROM python:3.11

WORKDIR /
COPY requirements.txt /
COPY src/ /

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 4003

CMD [ "--host", "0.0.0.0", "--port", "4003" ]
ENTRYPOINT [ "uvicorn" , "services:app"]
