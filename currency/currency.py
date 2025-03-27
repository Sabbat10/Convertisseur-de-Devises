import requests

def convertir_monnaie(montant, devise_cible):
    try:
        # 🔹 URL de l'API pour récupérer les taux de change à partir de l'EUR
        url = "https://api.exchangerate-api.com/v4/latest/CDF"
        reponse = requests.get(url)
        data = reponse.json()

        # 🔹 Vérifier si la devise cible existe dans la réponse de l'API
        if devise_cible in data["rates"]:
            taux = data["rates"][devise_cible]
            montant_converti = montant * taux
            print(f"✅ {montant} CDF = {montant_converti:.2f} {devise_cible} (Taux: {taux:.4f})")
        else:
            print(f"❌ Erreur : La devise '{devise_cible}' n'est pas disponible.")
    
    except Exception as e:
        print(f"❌ Erreur : {e}")
