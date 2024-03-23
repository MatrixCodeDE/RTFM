FROM python:3.11-alpine

EXPOSE 6001

# Preparations
RUN mkdir /ctf
WORKDIR /ctf

# Install requirements
COPY files/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Run app
COPY files/challenge.py ./
COPY files/flag.txt ./
ENTRYPOINT [ "python", "./challenge.py"]
