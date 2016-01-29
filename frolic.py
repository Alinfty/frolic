#!/usr/bin/env python3

from socket import *
import sys
#import parser

if __name__=="__main__":
	host=''
	port=80
	BUFSIZE=1024

	s=socket(AF_INET, SOCK_STREAM)
	s.bind((host,port))
	s.listen(5)

	try:
		while 1:
			print ("waiting...")
			conn, addr=s.accept()
			print ('Connected by', addr)
	
			while 1:
				data=conn.recv(BUFSIZE)
				if not data: break
				print ("received data:", data)
				conn.send(bytes("HTTP/2.0 200 OK\nContent-Type: text/plain\nContent-Length: 11\n\nHello world", 'utf8'))
				print("send complete")
			conn.close()

	except KeyboardInterrupt:
		print ("keyboard Interrupted!")
		s.close()
