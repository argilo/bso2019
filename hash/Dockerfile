FROM python:slim
WORKDIR /app
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY server.py rsa.py ./
COPY static/ ./static/
COPY templates/ ./templates/
RUN groupadd -r app && useradd -r -g app app
USER app
EXPOSE 5000
CMD [ "./server.py" ]
