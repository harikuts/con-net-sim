"""
Transmission Service: Sends out messages to other connected nodes.

Phase 1: Basic Operation
It should just send a generic broadcast message.
"""

# Globals
NODELIST_FN = "nodelist.txt"
PORT = 1245

import time
import socket
import random

# Get hostnames
with open(NODELIST_FN, 'r') as f:
    nodelist = f.read().strip().split()

# Messaging loop.
while True:
    for host in nodelist:
        time.sleep(random.randint(0, 5))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, PORT))
            s.send(f"Hello! - {socket.gethostbyname(socket.gethostname())}".encode("utf-8"))
            s.close()
        except Exception as e:
            pass
            # print(f"Failed to connect to {host}. Skipping.")