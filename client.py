import socket

host = "10.146.37.58"
port = 8080                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#s.sendall(b'Hello, world')
#s.sendall(b'Hello, world1')
data = s.recv(1024)
s.close()
print('Received', repr(data))
