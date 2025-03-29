import sys
import socket
import multiprocessing
import numpy as np
import scapy.config
import scapy.all
import atexit

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
UDP_ListenPort = 6969
UDP_SendPort = 8794

# Scan for Devices
def NetworkSearch():
    return
def scan_and_print_neighbors(net, interface, timeout=5):
    logger.info("arping %s on %s" % (net, interface))
    try:
        ans, unans = scapy.layers.l2.arping(net, iface=interface, timeout=timeout, verbose=True)
        for s, r in ans.res:
            line = r.sprintf("%Ether.src%  %ARP.psrc%")
            try:
                hostname = socket.gethostbyaddr(r.psrc)
                line += " " + hostname[0]
            except socket.herror:
                # failed to resolve
                pass
            logger.info(line)
    except socket.error as e:
        if e.errno == errno.EPERM:     # Operation not permitted
            logger.error("%s. Did you run as root?", e.strerror)
        else:
            raise
# Host Game

# Find Host
def FindHost():
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
    
    exit
    