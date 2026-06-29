// On se positionne sur la base de données admin pour créer le root
db = db.getSiblingDB('admin');

// 1. L'ADMINISTRATEUR (Utilise les variables Docker)
db.createUser({
  user: process.env.MONGO_USER,
  pwd: process.env.MONGO_PASS,
  roles: [{ role: "root", db: "admin" }]
});

// On bascule sur la base médicale
db = db.getSiblingDB('Healthcare');

// 2. USER_MEDICAL (Le mot de passe sera haché par MongoDB)
db.createUser({
  user: "User_Medical",
  pwd: process.env.MEDICAL_PASS,
  roles: [{ role: "readWrite", db: "Healthcare" }]
});

// 3. ANALYSTE (Le mot de passe sera haché par MongoDB)
db.createUser({
  user: "Analyste",
  pwd: process.env.ANALYST_PASS,
  roles: [{ role: "read", db: "Healthcare" }]
});

print("✅ Structure des utilisateurs créée avec succès (Passwords via Env) !");