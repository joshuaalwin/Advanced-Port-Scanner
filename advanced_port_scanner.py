#!/usr/bin/python

from socket import * 
import optparse
from threading import *



def connScan(target_host,port):
	try:
		sock=socket(AF_INET,SOCK_STREAM) 
		sock.connect((target_host,port))
		print "\n [+] %d/tcp open" %port
	except:
		print "\n [-] %d/tcp Closed" %port

	finally:
		sock.close()



def PortScan(target_host,target_ports):

	# Resolving hostname by IP and IP by hostname
 
	try:
		target_IP=gethostbyname(target_host)
	except:
		print "Couldn't resolve host %d" %target_host

	try:
		target_name=gethostbyaddr(target_IP)
		print "\n[+] Scan results For :" +target_Name[0]
	except:
		print "\n[+]  Scan Results For : " +target_IP

	setdefaulttimeout(1)
	for port in target_ports:
		t=Thread(target=connScan, args=(target_host,int(port)))  # Run a connsScan function to scan the ports
		t.start()


def main():

	# For command line argu,ents

	parser=optparse.OptionParser('Usage of Program :' + '-H <target_host> -p <target port>')
	parser.add_option('-H',dest="target_host",type='string',help="Destination of Target Host")
	parser.add_option('-p',dest="target_port",type='string',help="Target ports separated by comma")
	(options,args)=parser.parse_args()


	target_host=options.target_host
	target_ports=str(options.target_port).split(",") # Splitting each port to be scanned by comma

	# Scanning of port
	if (target_host==None) | (target_ports[0]==None): # If there's no Host or Port given, Printing the help
		print parser.usage
		exit(0)

	PortScan(target_host,target_ports)

if __name__ == "__main__":
	main()
