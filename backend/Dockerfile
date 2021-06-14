
FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk update
RUN apk add build-base postgresql-dev make gcc python3-dev musl-dev
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
