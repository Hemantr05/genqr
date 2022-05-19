FROM python:3.8-slim

WORKDIR /app

RUN apt update -y && \
    apt install build-essentials -y && \
    pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app
ENV FIRESTORE_SERVICE_ACCOUNT=test-ec22b-firebase-adminsdk-fezwt-61803c7945.json

EXPOSE 8080

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]