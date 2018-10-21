FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /rest-service
WORKDIR /rest-service
ADD . /rest-service
RUN pip install -r /rest-service/src/requirements.txt
ENTRYPOINT ["python"]
CMD ["/rest-service/src/main.py"]
