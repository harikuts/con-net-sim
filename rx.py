"""
Receiver Service: Accepts messages from other nodes and saves them.

Phase 1: Basic Operation
It should just accept incoming messages. Kinda like a server.
"""

# File information.
NODELIST_FN = "nodelist.txt"
# Arbitrary network values.
PORT = 1245

import socket

# Get information from nodelist.
with open(NODELIST_FN, 'r') as f:
    nodelist = f.read().strip().split()

# Get network interface information.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
# Choose arbitary port.
port = PORT

# Bind, listen, and connect to the port.
s.bind((host, port))
s.listen(len(nodelist))

# Looping listening service.
while True:
    # Accept a connection.
    conn, address = s.accept()
    print(f"Connected to {address}!")
    # Get stream of data.
    while True:
        data = conn.recv(1024).decode()
        # Break if no more data is streaming.
        if not data:
            break
        print (f"({address}) {data}")
    conn.close()