FROM python:3.10




# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /App/requirements.txt

WORKDIR /App

RUN pip install --no-cache-dir --upgrade -r /App/requirements.txt

# We also copy the required files and folders

COPY ./App /App


EXPOSE 8000

CMD ["python3", "main.py"]

