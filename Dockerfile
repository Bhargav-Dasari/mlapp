FROM arm64v8/python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]