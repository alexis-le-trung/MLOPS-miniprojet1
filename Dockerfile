FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY exercice0.py .
COPY regression.joblib .

CMD ["fastapi", "dev","exercice0.py", "--host", "0.0.0.0", "--port", "8000"]
