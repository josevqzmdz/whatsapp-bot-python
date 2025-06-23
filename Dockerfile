FROM alpine:latest

LABEL maintainer="${AUTHOR_EMAIL}"

WORKDIR /whatsapp_bot

COPY ./ ./
# https://stackoverflow.com/questions/62554991/how-do-i-install-python-on-alpine-linux
RUN apk update && \
    apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    python3 -m pip install --upgrade pip numpy && \
    python3 -m pip install --no-cache-dir --upgrade -r requirements.txt 
    

EXPOSE 80 443 8080

CMD ["python", "src/app.py"]