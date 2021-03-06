import getpass
import sys
import telnetlib

HOST = "None"
tn = telnetlib.Telnet(None)
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip address 10.10.10.1 255.255.255.255\n")
tn.write("int loop 1\n")
tn.write("ip address 20.20.20.2 255.255.255.255\n")
tn.write("router ospf 100\n")
tn.write("network 0.0.0.0 255.255.255.255 area 0\n")
tn.write("end\n")
tn.write("exit\n")

print (tn.read_all())