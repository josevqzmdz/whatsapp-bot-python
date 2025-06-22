FROM python:3.11-slim

LABEL maintainer="${AUTHOR_EMAIL}"

WORKDIR /whatsapp_bot

COPY ./ ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80 443 8080

CHD ["python", "src/app.py"]