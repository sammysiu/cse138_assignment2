# Copied from Docker's Python Development Tutorial(s)

# set base image (host OS)
FROM python:3.8-slim

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# Allow container to listen to port 13800
EXPOSE 13800

# command to run on container start
CMD [ "python", "./manage.py", "runserver", "0:13800" ]

#############################

# # first stage
# FROM python:3.8 AS builder
# COPY requirements.txt .

# # install dependencies to the local user directory (eg. /root/.local)
# RUN pip install --user -r requirements.txt

# # second unnamed stage
# FROM python:3.8-slim
# WORKDIR /code

# # copy only the dependencies installation from the 1st stage image
# COPY --from=builder /root/.local/bin /root/.local
# COPY ./src .

# # update PATH environment variable
# ENV PATH=/root/.local:$PATH

# # Allow container to listen to port 8081
# EXPOSE 8081

# CMD [ "python", "./server.py" ]