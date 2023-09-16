FROM python
WORKDIR /home/
COPY . .
RUN  pip install -r server-requirements.txt
ENTRYPOINT ["uvicorn","server:app"]