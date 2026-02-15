import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

# VIOLAZIONE 1: Hardcoded Secret (CWE-798)
AWS_KEY = "AKIA1234567890SECRET" 

@app.route('/ping')
def ping():
    # VIOLAZIONE 2: Command Injection (CWE-78)
    address = request.args.get('address')
    # Bandit odierà questa riga: shell=True
    subprocess.call("ping -c 1 " + address, shell=True) 
    return "Ping sent!"

if __name__ == '__main__':
    app.run()