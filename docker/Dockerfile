FROM python:3.8
#VOLUME /app
#WORKDIR Users/dkyse/Desktop/Tesing/docker
COPY . /app
#CMD mvn spring-boot:run
RUN apt-get update && \
   apt-get install -y python3

    ADD requirements.txt /
    RUN pip3 install -r /requirements.txt

RUN pip install --upgrade pip
#RUN python  -m pytest
CMD ["pytest", "./app/tests/functional/tests_login.py"]


