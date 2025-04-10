# NOTE: GUI is not supported !
# Use an official Python base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy your code into the container
COPY main.py src/ app/
COPY src/ ./app/src/

# Set the default command to run your app
CMD ["/bin/sh"]
