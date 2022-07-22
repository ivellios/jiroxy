FROM python:3.10.5-alpine

COPY ./jiroxy /jiroxy

CMD ["python", "/jiroxy/main.py"]
