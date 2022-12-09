FROM ubuntu:focal


RUN apt-get update -y;\
apt install python3-pip -y;

RUN useradd app;
USER app

WORKDIR /app

COPY . .

USER root
RUN pip3 install -r requirements.txt;

USER app

EXPOSE 3000 

CMD ["waitress-serve", "waitress_server:app"]