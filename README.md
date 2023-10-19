# Projet de Recommandations de Voyages

Ce projet est une application Django destinée à recommander des destinations de voyage en fonction des préférences des
utilisateurs et de leur budget. Il inclut également des fonctionnalités de réservation de voyages pour les utilisateurs
authentifiés.

## Configuration requise

- Python 3.x
- Django 4.x
- Packages Python (voir `requirements.txt`)

## Installation

1. Accédez au répertoire du projet :
   cd votreprojet

2. Installez les dépendances Python depuis requirements.txt :
   pip install -r requirements.txt

3. Appliquez les migrations de la base de données :
   python manage.py migrate

4. Lancez le serveur de développement Django :
   python manage.py runserver

5. Accédez au site Web à l'adresse http://localhost:8000/.

Utilisation
Création de compte : Les utilisateurs peuvent créer un compte avec leur nom d'utilisateur et mot de passe.
Profil utilisateur : Les utilisateurs peuvent ajouter leurs préférences de voyage et leur budget dans leur profil.
Destinations : Parcourez les destinations de voyage recommandées et consultez les détails.
Réservations : Les utilisateurs authentifiés peuvent effectuer des réservations de voyages pour les destinations.
Endpoints API

L'application expose une API REST avec les endpoints suivants :
/api/userprofile/ : CRUD pour les profils d'utilisateurs.
/api/destinations/ : CRUD pour les destinations de voyage.
/api/bookings/ : CRUD pour les réservations de voyages.

Pour accéder à l'API, vous pouvez utiliser des outils comme Postman ou cURL.
Configuration de la base de données
Ce projet est configuré pour utiliser SQLite par défaut. Vous pouvez le modifier dans les paramètres de base de
données (settings.py) en utilisant d'autres bases de données comme PostgreSQL ou MySQL.
 
