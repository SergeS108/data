# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 17:50:36 2025

@author: abesa
"""
"""
import os
import requests
Api_key= os.getenv("TMDB_API_KEY")
if not Api_key:
    raise ValueError("Clé API non trouvée. Vérifie ta variable d'environnement")
url = "https://api.themoviedb.org/3/movie/popular"
params = {"api_key": Api_key, "language": "fr-FR"}
response =requests.get(url, params=params)
data= response.json()
print("Premier film :", data["results"][0]["title"]) #[0]: c'est pour dire prend le premier élément de la liste
"""
import os
import requests
api_key = os.getenv("TMDB_API_KEY")
url= "https://api.themoviedb.org/3/movie/upcoming"
params = {"api_key": api_key, "language": "fr-FR", "page": 1}
try:
     response = requests.get(url, params =params, timeout =10)
     response.raise_for_status()
     data = response.json()
     
     results = data.get("results", [])
     if not results:
         print("Aucun film trouvé")
     else:
         for i in range (0,10):
            first_title = results[i].get("title", "Titre non diponible")
            print("le", i,"ème films est :", first_title)
except requests.exceptions.RequestException as e:
    print("Erreur lors de la requete HTTP :", e)
except ValueError:
    print("Réponse non-JSON ou JSON invalide")