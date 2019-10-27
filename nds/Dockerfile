FROM python:slim
WORKDIR /app
COPY nds.py server.py flag.txt ./
RUN groupadd -r app && useradd -r -g app app
USER app
EXPOSE 9999
CMD [ "./server.py" ]
