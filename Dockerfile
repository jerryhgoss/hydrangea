FROM python:3.10

WORKDIR /usr/src/app

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt ./

COPY ./.env ./


RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# We also copy the required files and folders

ADD ./App ./App

EXPOSE 8000

CMD ["python3", "App/main.py"]