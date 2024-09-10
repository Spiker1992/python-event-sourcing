FROM python:slim

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]