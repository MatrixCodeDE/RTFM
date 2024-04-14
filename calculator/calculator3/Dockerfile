FROM python:3.11-alpine

EXPOSE 6003

# Preparations
RUN mkdir /ctf && \
    adduser -h /ctf -D -H ctf -u 1001 && \
    chown -R root:root /ctf && \
    chmod -R +r /ctf
WORKDIR /ctf

# Install requirements
COPY files/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Run app
COPY files/challenge.py ./
COPY files/flag.txt ./

RUN chown root challenge.py && \
    chown root flag.txt && \
    chmod +r challenge.py && \
    chmod +r flag.txt

USER ctf
ENTRYPOINT [ "python", "./challenge.py"]
