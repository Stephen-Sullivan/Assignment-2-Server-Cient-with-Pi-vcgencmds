# Runs on Pc, directly from Thonny
# The client

import socket
import json

s = socket.socket()
host = '1.1.1.1'  # ip of raspberry pi, running the server
port = 5001
s.connect((host, port))

data = s.recv(4096)  # Increase buffer size if needed
data_str = data.decode('utf-8')  # Decode byte data to string

if data_str:
    json_data = json.loads(data_str)  # Load string as JSON
    for key, value in json_data.items():
        print(f"{key}: {value}")

s.close()
