FROM python:3.9

MAINTAINER Andreas Hallof, andreas.hallof@googlemail.com

RUN apt-get update
# Ich möchte gerne wenn ich den Container interaktiv verwende,
# dort auch mit vim Dateien bearbeiten können.
RUN apt-get --yes install vim

# Ich möchte gerne openssl mit ein paar mehr Depencies installieren.
RUN apt-get --yes install apt-utils
RUN apt-get --yes install libmpc-dev libmpfr-dev libmpfr-doc 
RUN apt-get --yes install libldap2-dev libsasl2-dev
RUN apt-get --yes install python-cryptography python3-cbor

RUN pip install pyOpenSSL 

COPY ./ /as-wechsel
WORKDIR /as-wechsel

RUN pip install -r requirements.txt

CMD ["echo", "Starte mich interaktiv mit 'docker run -it as-wechsel:0.1 /bin/bash'"]

