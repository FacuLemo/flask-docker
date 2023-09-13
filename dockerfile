FROM python:3.8-alpine
COPY . /flask-docker
WORKDIR /flask-docker

RUN pip install -r requirements.txt
EXPOSE 5020
ENTRYPOINT [ "python3" ]
CMD ["app.py"]