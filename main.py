from currency.currency import convertir_monnaie

# 🔹 Demander à l'utilisateur d'entrer le montant et la devise cible
try:
    montant = float(input("💶 Entrez le montant en CDF : "))
    devise_cible = input("🌍 Entrez la devise cible (ex: USD, GBP, JPY, CAD, ) : ").upper()
    
    convertir_monnaie(montant, devise_cible)
except ValueError:
    print("❌ Erreur : Veuillez entrer un montant valide.")

# 🔹 Appel de la fonction avec les valeurs entrées



