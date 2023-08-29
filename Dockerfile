FROM python:3-alpine3.18

#working directory:
#WORKDIR src

#to COPY the remote file at working directory in container
COPY src/Script_V1_python.py ./
COPY src/weathercode_dictionary.py ./

RUN apk add --no-cache bash
RUN pip install --upgrade pip
RUN pip install requests

CMD ["/bin/bash"]
