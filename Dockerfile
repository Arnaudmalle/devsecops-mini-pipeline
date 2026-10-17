# VULN-4 : image complète, tag flottant "latest"
FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 8000

# VULN-4 : exécution en root
USER root

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
