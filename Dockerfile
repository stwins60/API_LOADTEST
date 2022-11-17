FROM python:3.9

WORKDIR /src
COPY . .
# COPY ./app/requirements.txt /src/requirements.txt



RUN pip --no-cache-dir install -r /src/requirements.txt

EXPOSE 5000
ENV FLASK_APP app
ENV FLASK_ENV development
ENV DEBUG=1
ENV PYTHONUNBUFFERED=1



CMD [ "python", 'app.py']
# CMD [ "flask", 'run']