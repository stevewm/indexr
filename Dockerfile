FROM frolvlad/alpine-python3:latest

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY run.py /app
COPY indexr /app/indexr

CMD python /app/run.py
