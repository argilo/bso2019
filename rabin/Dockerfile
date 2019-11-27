FROM python:slim
WORKDIR /app
COPY rabin.py server.py ./
RUN groupadd -r app && useradd -r -g app app
USER app
EXPOSE 7979
CMD [ "./server.py" ]
