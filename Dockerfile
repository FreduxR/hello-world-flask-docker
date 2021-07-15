FROM python:3.7
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
WORKDIR /app
COPY . .
ENTRYPOINT ["python", "app.py"]
EXPOSE 5000