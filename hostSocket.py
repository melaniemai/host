import socket
import sys


def getHostName():
    hostname = socket.gethostname()
    print("Host Name for this machine : " + hostname)

def getIP():
    # --------------------- get IPv4 ----------------------
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    k = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        ipList = []
        # doesn't even have to be reachable
        s.connect(('8.8.8.8', 80))
        k.connect(('10.255.255.255', 1))
        if(s.getsockname()[0] == k.getsockname()[0]):
            ipList.append(s.getsockname()[0])
        else:
            ipList.append(s.getsockname()[0])
            ipList.append(k.getsockname()[0])
    except:
        ipList = '127.0.0.1'
    finally:
        s.close()

    print("IPv4 Address Assigned to this machine are :")
    for i in ipList:
        print("\t " + i)

    # --------------------- get IPv6 ----------------------
    print("IPv6 Address Assigned to this machine are :")
    j = 0
    while j < len(ipList):
        ipadd = socket.getaddrinfo(ipList[j], 8080)
        print("\t " + ipadd[0][4][0])
        j += 1


getHostName()
getIP()
