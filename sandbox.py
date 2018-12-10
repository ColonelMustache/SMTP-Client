import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 80))
sock.send('GET / HTTP/1.1')
print sock.recv(4096)
sock.close()
sock = socket.socket()
sock.connect(('127.0.0.1', 53))
sock.send('hello')
