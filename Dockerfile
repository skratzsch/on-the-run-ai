FROM python:3.12-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Projektdateien kopieren
COPY . .

# Port für Django (Standard: 8000)
EXPOSE 8000

# Startbefehl (kann angepasst werden)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
