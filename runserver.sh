#!/bin/bash

source .env/bin/activate

cd src/
# Exécuter la commande pour démarrer le serveur Django
gnome-terminal -- python3.11 manage.py runserver --noreload


sleep 2  # Attendre quelques secondes pour que le serveur démarre

# Ouvrir le navigateur Web par défaut
xdg-open "http://127.0.0.1:8000/"
