# Use the Python3.7.2 container image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# create a non-privileged user
RUN adduser -D bitwalla

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Create a uwsgi log directory and files
RUN mkdir /var/log/uwsgi
RUN touch /var/log/uwsgi/uwsgi_access.log
RUN touch /var/log/uwsgi/uwsgi_error.log

USER bitwalla

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]