# test_ota.py
import ota_client
import os

def test_download_update():
    assert ota_client.download_update() == True
    assert os.path.exists('downloaded_update.bin')

def test_install_update():
    # Simule qu'une mise à jour a déjà été téléchargée
    with open('downloaded_update.bin', 'w') as f:
        f.write("dummy data")
    assert ota_client.install_update() == True
    assert os.path.exists('installed_update.bin')
