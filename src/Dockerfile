#Docker file for backend image 

FROM python:3-alpine3.18

WORKDIR src

COPY Script_V1_python.py ./
COPY weathercode_dictionary.py ./

RUN pip install requests
RUN make ./Script_V1_python.py

CMD ["python3"]
