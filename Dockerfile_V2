FROM python:3-alpine3.18

#working directory:
WORKDIR /Wind/src

#to COPY the remote file at working directory in container
COPY Script_V1_python.py ./
COPY weathercode_dictionary.py ./

RUN apk add --no-cache bash
RUN pip install --upgrade pip
RUN pip install requests

CMD ["/bin/bash"]
