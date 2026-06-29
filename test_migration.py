import pytest

# On teste si la conversion du montant (Billing Amount) fonctionne
def test_billing_conversion():
    valeur_csv = "150.50"
    resultat = float(valeur_csv)
    assert isinstance(resultat, float)
    assert resultat == 150.50

# On teste le formatage d'un nom de patient
def test_patient_name_clean():
    nom_sale = "  M. DURAND  "
    nom_propre = nom_sale.strip()
    assert nom_propre == "M. DURAND"