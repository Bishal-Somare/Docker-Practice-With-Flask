# base image
FROM python:3.10

# set working directory
WORKDIR /app

# copy all files into /app folder inside the container
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# expose flask port
EXPOSE 5000

# command to run the app
CMD ["python", "app.py"]
