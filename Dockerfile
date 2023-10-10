#Docker file for frontend image 

FROM python:3-alpine3.18

EXPOSE 80/tcp

COPY forms.py ./
COPY frontend.py ./
COPY templates/* ./

RUN pip install request
RUN pip install Flask

CMD ["python3", "./frontend.py"]
