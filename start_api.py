"""
Starter file for Streamlit Sharing to get the API up and running.
This launches each time the app is refreshed, but only restarts the API
if it isn't detected.
"""

import subprocess
import requests
import os 


#api_port=os.environ.get('PORT')
api_port=8000

api_check_url = "http://0.0.0.0:"+str(api_port)

try:
    r = requests.get(api_check_url)
    if r.ok:
        print("API already started")
except requests.exceptions.ConnectionError:
    print("Starting the API")
    cmd = ["uvicorn", "api:app"]
    subprocess.Popen(cmd, close_fds=True)
