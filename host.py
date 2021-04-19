import socket
import ipaddress
import platform
import struct


# get hostname 
# hostname = socket.gethostname()
# print("Host Name for this machine : " + hostname)

# # find IP4 address(s)
# ip4add = socket.gethostbyname_ex(hostname)[-1]
# print("IPv4 Address Assigned to this machine are :")
# for i in ip4add:
#      print("    " + i)

# # find IP6 address(s)
# print("IPv6 Address Assigned to this machine are : ")
# prefix = "::ffff:"
# for _ in ip4add:
#      print("    " + prefix + _)

# def get_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         # doesn't even have to be reachable
#         s.connect(('10.255.255.255', 1))
#         IP = s.getsockname()[0]
#     except:
#         IP = '127.0.0.1'
#     finally:
#         s.close()
#     return IP

typeOfOS = int(input("Press '1' if OS is Unix/Mac\nPress '2' for Windows: "))

if(typeOfOS == 1):
     import fcntl
     def getHostName():
          hostname = socket.gethostname()
          print("Host Name for this machine : " + hostname)

     def getIPv4and6():
          address = socket.gethostbyname(socket.gethostname())
          s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          try:
               # doesn't even have to be reachable
               s.connect(('10.255.255.255', 1))
               IP = s.getsockname()
          except:
               IP = '127.0.0.1'
          finally:
               s.close()
     
          print("IPv4 Address Assigned to this machine are :")
          print("    " + address)
          if(len(IP) != 0 and IP[0] != address):
               print("    " + IP[0])


          ipadd = socket.getaddrinfo(address, None, socket.AF_INET6)[0][4][0]
          print("IPv6 Address Assigned to this machine are :")
          print("    " + ipadd)
          if(len(IP) != 0 and IP[0] != address):
               print("    " + socket.getaddrinfo(IP[0], None, socket.AF_INET6)[0][4][0])


          # print(socket.gethostbyname_ex(socket.gethostname())[-1])

          getHostName()
          getIPv4and6()

# def getHostName():
#      hostname = socket.gethostname()
#      print("Host Name for this machine : " + hostname)

# def getIPv4and6():
#      address = socket.gethostbyname(socket.gethostname())
#      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#      try:
#         # doesn't even have to be reachable
#         s.connect(('10.255.255.255', 1))
#         IP = s.getsockname()
#      except:
#         IP = '127.0.0.1'
#      finally:
#         s.close()
     
#      print("IPv4 Address Assigned to this machine are :")
#      print("    " + address)
#      if(len(IP) != 0 and IP[0] != address):
#           print("    " + IP[0])


#      ipadd = socket.getaddrinfo(address, None, socket.AF_INET6)[0][4][0]
#      print("IPv6 Address Assigned to this machine are :")
#      print("    " + ipadd)
#      if(len(IP) != 0 and IP[0] != address):
#           print("    " + socket.getaddrinfo(IP[0], None, socket.AF_INET6)[0][4][0])


# # print(socket.gethostbyname_ex(socket.gethostname())[-1])

# getHostName()
# getIPv4and6()
