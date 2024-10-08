from flask import Flask, send_from_directory
import os

app = Flask(__name__)

UPDATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../updates')

# End point pour distribuer la mise à jour OTA
@app.route('/ota/update', methods=['GET'])
def send_update():
    # Simule l'envoi d'un fichier de mise à jour depuis le répertoire 'updates'
    return send_from_directory(directory=UPDATE_DIR, path='update_v1.1.bin')

if __name__ == '__main__':
    app.run(debug=True)
