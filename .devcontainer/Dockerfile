FROM python:3.12-slim
WORKDIR /workspace
COPY . .
WORKDIR /workspace/src
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y git
