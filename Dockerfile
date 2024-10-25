FROM python:3-alpine3.19
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 90
CMD ["python", "galo.py"]