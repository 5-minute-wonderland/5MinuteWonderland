import sys
import socket
import multiprocessing
import numpy as np
import ipaddress
import os

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
UDP_ListenPort = 6969
UDP_SendPort = 8794
network = ipaddress.ip_network

# Scan for Devices
def NetworkSearch():
    return

# Host Game

# Find Host
def FindHost():
    return
# Send packets
def SendPackets():
    return

# main method
if __name__=="__main__":
    response = input("Would You like to host or join a game?: ")
    print(network)
    while response.upper() != "HOST" and response.upper() != "JOIN":
        response = input("Invalid response: Type \"Host\" to host or \"Join\" to join ")
        print(network)
    devices = []
    for device in os.popen('arp -a'): devices.append(device)
    print(devices)
    print(ip)
    exit