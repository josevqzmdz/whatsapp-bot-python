FROM alpine:latest

LABEL maintainer="${AUTHOR_EMAIL}"

WORKDIR /whatsapp_bot

COPY ./ ./

# install python
# https://stackoverflow.com/questions/62554991/how-do-i-install-python-on-alpine-linux
RUN apk update && \
    apk add --update --no-cache python3 && ln -sf python3 -m venv /usr/bin/python && \
    python3 -m venv ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    python3 -m pip install --upgrade pip numpy 

# install conda
# https://pythonspeed.com/articles/activate-conda-dockerfile/

FROM continuumio/miniconda3

WORKDIR /app

# creates the environment
COPY compose.yaml .
RUN conda env create -f compose.yaml

# make RUN commands use the new environment
SHELL ["conda", "run", "-n", "conda_env", "/bin/bash", "-c"]

COPY "src/app.py"

# install other requirements
RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt 

EXPOSE 80 443 8080

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "conda_env", "python", "src/app.py"]
CMD ["python", "src/app.py"]