# ota_client.py
import requests
import os

# URL du serveur OTA
OTA_URL = "http://localhost:5000/ota/update"

# Fonction pour télécharger la mise à jour
def download_update():
    try:
        response = requests.get(OTA_URL)
        response.raise_for_status()
        with open('downloaded_update.bin', 'wb') as file:
            file.write(response.content)
        print("Mise à jour téléchargée avec succès.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement de la mise à jour : {e}")
        return False


# Fonction pour installer la mise à jour
def install_update():
    if os.path.exists('downloaded_update.bin'):
        print("Installation de la mise à jour...")
        # Simule l'installation (par exemple, copie du fichier dans un autre répertoire)
        os.rename('downloaded_update.bin', 'installed_update.bin')
        print("Mise à jour installée avec succès.")
        return True
    else:
        print("Aucune mise à jour disponible pour l'installation.")
        return False

if __name__ == '__main__':
    if download_update():
        install_update()
