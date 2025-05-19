FROM python:3.11-slim

WORKDIR /app

COPY gluetun_reload.py .

RUN pip install requests

CMD ["python", "gluetun_reload.py"]