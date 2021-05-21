FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /urlShort
WORKDIR /urlShort
ADD requirements.txt /urlShort/
RUN pip install pip==21.1.1 && pip install -r requirements.txt
ADD . /urlShort/
