import os
import subprocess
# import shlex  <-- Non serve se usiamo la lista in subprocess
from flask import Flask, request
 
app = Flask(__name__)
 
# FIX 1: Usa Variabile d'Ambiente (Niente segreti nel codice!)
AWS_KEY = os.environ.get("AWS_ACCESS_KEY_ID") 
 
@app.route('/ping')
def ping():
    address = request.args.get('address')
 
    if not address or ";" in address:
        return "Invalid address", 400
 
    try:
        # FIX 2: Niente shell=True, usa una lista di argomenti
        subprocess.run(["ping", "-c", "1", address], check=True)
    except Exception:
        return "Ping failed"
 
    return "Ping sent!"