FROM python:slim
RUN apt-get update && apt-get install -y imagemagick
WORKDIR /app
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY server.py rsa.py ./
COPY templates/ ./templates/
RUN groupadd -r app && useradd -r -g app app
USER app
EXPOSE 5000
CMD [ "./server.py" ]
