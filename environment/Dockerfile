FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD config/requirements.pip /config/
RUN pip install -r /config/requirements.pip
RUN mkdir /easystarter_web
WORKDIR /easystarter_web
RUN mkdir /static
