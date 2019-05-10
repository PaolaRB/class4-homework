FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pandas

COPY data ./data
COPY my_csv_reader_docker.py .

CMD ["python3","-u","my_csv_reader_docker.py"]
