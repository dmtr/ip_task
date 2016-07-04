FROM python:3.5.1
RUN mkdir -p /app/ip_task
ADD ip_task /app/ip_task/
RUN pip install --upgrade pip
WORKDIR /app
RUN pip3 install -r ip_task/requirements.txt
