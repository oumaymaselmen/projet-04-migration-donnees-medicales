# Utilisation d'une image Python officielle légère
FROM python:3.9-slim

# Définition du dossier de travail dans le conteneur
WORKDIR /app

# Copie du fichier requirements pour installer les bibliothèques d'abord
COPY requirements.txt .

# Installation des dépendances (Pandas, Pymongo, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Copie de tout le projet (le script migrate.py et le dataset CSV)
COPY . .

# La commande qui lancera la migration automatiquement
CMD ["python", "migrate.py"]