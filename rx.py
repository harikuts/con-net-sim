"""
Transmission Service: Sends out messages to other connected nodes.

Phase 1: Basic Operation
It should just send a generic broadcast message.
"""

# Globals
NODELIST = "nodelist.txt"

import socket

# Get hostnames
with open(NODELIST, 'r') as f:
    nodelist = f.read().strip().split()

print(nodelist)