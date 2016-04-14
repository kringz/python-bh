import sys
import socket
import getopt
import threading
import subprocess

# define global variables

listen			= False
command			= False
upload 			= False
execute			= ""
target			= ""
upload_destination	= ""
port			= 0

def usage():
	print "Custom Net Tool"
	print
	print "Usage: netcat_alternative.py -t target_host -p host"
	print "-l --listen		- listen on [host]:[port] for incoming connections"
