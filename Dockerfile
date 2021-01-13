FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /omed
WORKDIR /omed
RUN python -m venv env
RUN /bin/bash -c "source env/bin/activate"
ADD requirements.txt /omed/
RUN pip install -r requirements.txt
ADD . /omed/