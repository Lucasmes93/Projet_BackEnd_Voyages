import requests

# URL d'endpoint d'authentification (assurez-vous de l'ajuster en fonction de votre configuration)
authentication_url = 'http://127.0.0.1:8000/api/token/'

# Informations d'identification de l'utilisateur
credentials = {
    'username': 'Lucas',
    'password': '123456',
}

# Effectuer la demande POST pour l'authentification
response = requests.post(authentication_url, data=credentials)

# Vérifier la réponse de l'API
if response.status_code == 200:
    # Si la demande est réussie, le jeton JWT est dans la réponse
    token_data = response.json()
    access_token = token_data.get('access')
    print(f"Jetons JWT d'accès : {access_token}")

    # Ajouter le jeton JWT dans l'en-tête pour les futures requêtes
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    # Vous pouvez utiliser cet en-tête dans vos futures requêtes, par exemple :
    # response = requests.get('https://votre-api.com/endpoint/', headers=headers)
else:
    print(f"Échec de l'authentification. Code d'état : {response.status_code}")
    print(response.text)
