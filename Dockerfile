FROM docker.io/library/python:latest
WORKDIR /home/
COPY . .
RUN  pip install -r server-requirements.txt
ENTRYPOINT ["uvicorn","server:app"]