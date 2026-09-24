#  Projet de Migration de Données Médicales - DataSoluTech

## 1. Contexte et Objectifs
Ce projet répond à une demande de modernisation pour un client médical gérant 55 500 dossiers de patients. L'objectif est de migrer un dataset CSV vers une base de données NoSQL **MongoDB** pour assurer la scalabilité et la portabilité grâce à **Docker**.

## 2. Environnement Technique
La solution repose sur une stack moderne et isolée pour éviter tout conflit de version :
* **Langage** : Python-3.13.5
* **Gestion des données** : Pandas-2.3.3 (pour le nettoyage et le typage)
* **Pilote de base de données** : PyMongo-4.15.5
* **Infrastructure** : Docker & Docker Compose (Docker Desktop)
* **Visualisation** : MongoDB Compass (via le port configuré `27019`)

## 3. Logique de la Migration
Le script garantit l'intégrité des données de santé :
* **Typage des dates** : Conversion des colonnes `Date of Admission` et `Discharge Date` en objets `DateTime`.
* **Typage numérique** : Conversion du champ `Billing Amount` en `float` pour les calculs financiers.
* **Normalisation** : Création automatique de la base `Healthcare` et de la collection `Patients`.



## 4. Architecture Docker & Persistance
Le projet utilise **Docker Compose** pour orchestrer deux services :
1. **`mongodb_container`** : Instance MongoDB isolée.
2. **`migration_script_container`** : Conteneur Python qui exécute la migration.

* **Volumes** : Un volume est utilisé pour assurer la **persistance des données** sur le disque local, garantissant que les données médicales ne sont pas perdues si le conteneur est supprimé.
* **Mappage de port** : Le service est exposé sur le port **27019** pour éviter les conflits avec des installations MongoDB locales pré-existantes.


## 5. Instructions d'Installation et Lancement
Pour déployer et exécuter la migration en une commande :

1.  **Pré-requis Sécurité** : Créez un fichier nommé `.env` à la racine du projet et ajoutez-y les lignes suivantes :
    ```env
    MONGO_USER=admin
    MONGO_PASS=SuperSecureHealth2026!
    ```
2.  Lancez **Docker Desktop**.
3.  Ouvrez un terminal à la racine du projet dans VS Code et tapez :
    ```bash
    docker-compose up --build
    ```
4.  **Vérification** : Une fois que le terminal affiche ` Migration réussie !`, la base est prête.
## 6. Accès aux Données
Pour consulter les 55 500 documents migrés :

* Ouvrez **MongoDB Compass**.
* Utilisez l'URI de connexion : mongodb://admin:SuperSecureHealth2026!@localhost:27019/?authSource=admin
* Cliquez sur le bouton **Refresh** pour faire apparaître la base **Healthcare**.
---

##  7. Schéma de la Base de Données (NoSQL)
Contrairement à une base SQL classique, MongoDB utilise des documents JSON flexibles. Pour ce projet, chaque document de la collection `Patients` suit cette structure :

```json
{
  "Patient_Name": "String",
  "Age": "Int32",
  "Gender": "String",
  "Blood_Type": "String",
  "Medical_Condition": "String",
  "Date_of_Admission": "Date",
  "Doctor": "String",
  "Hospital": "String",
  "Insurance_Provider": "String",
  "Billing_Amount": "Double",
  "Room_Number": "Int32",
  "Admission_Type": "String",
  "Discharge_Date": "Date",
  "Medication": "String",
  "Test_Results": "String"
  }
```
  ## 8. Système d’Authentification et Rôles

Pour sécuriser les données de santé, l'accès à MongoDB est protégé par une politique de contrôle d'accès basée sur les rôles (RBAC) et un mécanisme d'authentification robuste.

### **Protection des Secrets et Cryptage :**
* **Zéro Secret en clair** : Aucun mot de passe n'est stocké dans le code source sur GitHub. Les identifiants sont injectés via des **variables d'environnement** au moment du déploiement Docker.
* **Hachage SCRAM-SHA-256** : MongoDB utilise l'algorithme de hachage sécurisé SCRAM pour crypter les mots de passe. Une fois créés, les mots de passe ne sont plus lisibles en clair dans les fichiers de configuration de la base de données.

### **Rôles Utilisateurs créés :**
* **Admin (Root)** : Géré via les variables `${MONGO_USER}` et `${MONGO_PASS}`. Accès total pour la maintenance.
* **User_Medical** : Accès en lecture et écriture pour la gestion quotidienne des dossiers.
* **Analyste** : Accès en **lecture seule** (Read-Only) pour l'analyse statistique, garantissant qu'aucune donnée ne peut être modifiée par erreur.
## 9. Qualité Logicielle et Tests
Pour garantir l'intégrité des données médicales lors de la migration, le projet inclut des tests unitaires automatisés :
* **Framework utilisé** : `pytest`
* **Tests effectués** :
    * Validation de la conversion des montants financiers (Billing Amount).
    * Validation du nettoyage et du formatage des noms de patients.
* **Exécution** : Les tests sont conçus pour être lancés dans l'environnement Dockerisé, garantissant que le script de migration est stable avant l'injection en base de données.

## Résultats
Migration conteneurisée de données médicales avec contrôles qualité
