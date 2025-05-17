FROM python:3-slim-buster 

RUN mkdir -p /home/app
WORKDIR /home/app

RUN pip install flask 

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]





