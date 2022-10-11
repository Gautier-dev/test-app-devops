FROM python:3

ENV FLASK_APP=main.py
ENV FLASK_ENV=development 

RUN pip install Flask

WORKDIR /Flask-app

COPY . /Flask-app

EXPOSE 8080

CMD ["flask","run","-h","0.0.0.0","-p","8080"]
