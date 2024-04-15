FROM python:3.12-alpine
WORKDIR /app
COPY /src .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "-u", "main.py"]