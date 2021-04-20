import socket
import sys

def getHostName():
    hostname = socket.gethostname()
    print("Host Name for this machine : " + hostname)

def getIP():
    print("IPv4 Address Assigned to this machine are :")
    ipadd = socket.gethostbyname_ex(socket.gethostname())[-1]
    for i in ipadd:
        print("\t " + i)

    # --------------------- get IPv6 ----------------------
    print("IPv6 Address Assigned to this machine are :")
    ipadd2 = socket.getaddrinfo(socket.gethostname(), None)
    l = len(ipadd)
    for i in ipadd2[l:]:
        print("\t " + i[-1][0])

getHostName()
getIP()
