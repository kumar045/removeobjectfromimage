FROM python:3.7.4-slim-buster
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install lama-cleaner 
EXPOSE 8080
CMD lama-cleaner --model=lama --device=cpu --port=8080
