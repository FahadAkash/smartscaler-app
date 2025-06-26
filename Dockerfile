FROM  python:3.10-slim
WORKDIR /app
COPY Backend/app.py /app
RUN pip install flask
CMD [ "python" , "app.py" ]