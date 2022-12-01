FROM python:3.10



# We also copy the required files and folders

COPY ./App /App

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /App/requirements.txt

WORKDIR /App

RUN pip install --no-cache-dir --upgrade -r /App/requirements.txt

ENV PORT=8000

ENV ATLAS_URI=mongodb+srv://tzou2024:pswd@cluster0.ivgfrft.mongodb.net/?retryWrites=true&w=majority

ENV DB_NAME=hydro

RUN printenv

EXPOSE 8000

CMD ["python3", "main.py"]

