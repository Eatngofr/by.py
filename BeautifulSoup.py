# Importation des bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = 'https://lionofficiel.blogspot.com/'

# Envoi d'une requête HTTP à l'url spécifiée
response = requests.get(url)

# Vérification que la requête a bien réussi
if response.status_code == 200:
    # Création d'un objet BeautifulSoup pour analyser le contenu parsé
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraction des données selon le besoin, par exemple, récupérer tous les paragraphes
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print(paragraph.text)
else:
    print("Erreur lors de la récupération de la page")

