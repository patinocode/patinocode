FROM python:3.10-alpine

WORKDIR /app
COPY . .

ENTRYPOINT ["./main.py"]