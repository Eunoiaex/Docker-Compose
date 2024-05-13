FROM python:3.11

ENV FLASK_APP=flaskTutorial1.py

ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

RUN pip install flask-mysqldb

COPY . .

EXPOSE 5000

CMD ["python", "flaskTutorial1.py"]
