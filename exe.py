#!/usr/bin/env python3

import socket
import parser

if __name__=="__main++":
	host=''
	port=80
	BUFFER_SIZE=1024

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	s.listen(1)
	conn, addr=s.accept()
	print ('Connected by', addr)
	while 1:
		data=conn.recv(BUFFER_SIZE)
		if not data: break
		print ("received data:", data)
		conn.send("HTTP/2.0 200 OK\nContent-Type: text/plain\nContent-Length: 11\n\nHello world".encode('utf8'))
		print("send complete")
	conn.close()
