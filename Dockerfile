FROM python:2.7

MAINTAINER walter.arruda.alves@gmail.com

# -- Install Application into container:
RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt
#COPY Pipfile.lock Pipfile.lock

RUN pip install -r requirements.txt

#Copy app
COPY . /app

#Install modules
RUN python setup.py install
