import socket
import multiprocessing
import numpy as np
import scapy.config
import scapy.all
import atexit
import math
import nmap
import threading

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
UDP_ListenPort1 = 7001
UDP_ListenPort2 = 7002
UDP_ListenPort3 = 7003
UDP_SendPort = 8794


# Host devices will have an open port

# Scan for Devices
def NetworkSearch():
    return

def HandleClient(conn, addr):
    return

# Host Game
# MESSY With errors (inported from another project)
def PortListener(PortNumber):
    socklstn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socklstn.bind(('localhost', PortNumber))
    socklstn.listen(5)
    while True:
        try:
            conn, addr = socklstn.accept()
            thread = threading.Thread(target=HandleClient, args=(conn, addr))
            thread.start()
        
        
            message = conn.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received command from {addr}: {message}")  # Debugging output
            process_message(conn, addr, message)  # Passing addr here
        except Exception as e:
            print(f"Error with client {addr}: {e}")
            break
    socklstn.close()
    return


# Find Host
def FindHost():
    network = '10.0.0.0/8'
    scanner = nmap.PortScanner
    while True:
        scanner.scan(network, '7001-7003')
        for host in scanner.all_hosts():
            print(host)
        print("Type \"Refresh\" to refrsh")
        print("Type \"Cancel\" to cancel")
        print("Type the IP address to join that host")
        ip = input("Input: ")
        if input.upper() == "CANCEL":
            exit
        if input.upper() == "REFRESH":
            scanner.scan(network, '7001-7003')
            for host in scanner.all_hosts():
                print(host)
        else:
            try:    
                udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                udp_socket.bind(('localhost', 0))  # Bind to an available port
            except:
                return
            break
    return
# Send packets
def SendPackets():
    return


# Exit Handler: Runs when program exits
def exit_handler():
    print('My application is ending!')
atexit.register(exit_handler)


# main method
if __name__=="__main__":
    response = input("Would You like to host or join a game?: ")
    while response.upper() != "HOST" and response.upper() != "JOIN":
        response = input("Invalid response: Type \"Host\" to host or \"Join\" to join ")
    print(ip)
    for network, netmask, _, interface, address, _ in scapy.config.conf.route.routes:
        print("IP: %d" % network)
        print("Mask: %d" % netmask)
        # skip loopback network and default gw
        if network == 0 or interface == 'lo' or address == '127.0.0.1' or address == '0.0.0.0':
            continue

        if netmask <= 0 or netmask == 0xFFFFFFFF:
            continue
        
        #net = to_CIDR_notation(network, netmask)
        #if net:
        #    print(net)
            #scan_and_print_neighbors(net, interface)
    exit
    