FROM python:3


RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN apt-get install -y \
    vim

ARG PROJECT=myproject
ARG PROJECT_DIR=/var/www/${PROJECT}

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY Pipfile Pipfile.lock ./
RUN pip install -U pipenv
RUN pipenv install --system

COPY . .
RUN python manage.py migrate
RUN python manage.py initadmin
RUN python manage.py loaddata fixture

EXPOSE 80
ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "0:80"]
