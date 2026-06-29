import pandas as pd
from pymongo import MongoClient
import time
import os  # AJOUTÉ : Pour lire les variables d'environnement

def run_migration():
    # 1. Connexion à MongoDB sécurisée
    time.sleep(10)
    
    # RÉCUPÉRATION des secrets 
    user = os.getenv('MONGO_USER', 'admin') # 'admin' par défaut
    # Dans migrate.py
    password = os.getenv('MONGO_PASS', 'SuperSecureHealth2026!')

    # Construction de l'URI avec les variables
    # On garde @mongodb car c'est le nom de ton service dans le network Docker
    uri = f"mongodb://{user}:{password}@mongodb:27017/?authSource=admin"
    
    client = MongoClient(uri)    
    db = client["Healthcare"]
    collection = db["Patients"]

    # 2. Chargement du CSV
    print("Chargement du fichier CSV...")
    df = pd.read_csv("healthcare_dataset.csv")

    # 3. Nettoyage et Conversion 
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    df['Billing Amount'] = df['Billing Amount'].astype(float)

    # 4. Transformation en format JSON
    data_to_insert = df.to_dict(orient='records')

    # 5. Insertion dans la base
    collection.delete_many({}) 
    print(f"Insertion de {len(data_to_insert)} documents dans MongoDB")
    collection.insert_many(data_to_insert)
    
    print("✅ Migration réussie !")

if __name__ == "__main__":
    run_migration()