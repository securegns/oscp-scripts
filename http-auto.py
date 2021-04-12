# /bin/python3
import argparse

# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-http", "--http")
parser.add_argument("-https", "--https")
parser.add_argument("-ip", "--ip")

# Read arguments from command line
args = parser.parse_args()
 
http_ports = str(args.http).split(',')
https_ports = str(args.https).split(',')
ipaddr = args.ip

for i in http_ports:
# whatweb 
# nikto
# gobuster with 2.3-medium, seclists
for i in https_ports:
