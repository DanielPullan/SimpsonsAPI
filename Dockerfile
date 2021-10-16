FROM python:latest
WORKDIR /app
RUN pip3 install flask simplepush
COPY . . 
CMD python3 flasky.py
