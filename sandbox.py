import socket
HOSTNAME_SMTP_SERVER = 'networks.cyber.org.il'
PORT_SMTP = 587

"""
sock = socket.socket()
sock.connect(('127.0.0.1', 80))
sock.send('GET / HTTP/1.1')
print sock.recv(4096)
sock.close()
sock = socket.socket()
sock.connect(('127.0.0.1', 53))
sock.send('hello')
"""

server_ip = socket.gethostbyname(HOSTNAME_SMTP_SERVER)
client_sock = socket.socket()
client_sock.connect((server_ip, PORT_SMTP))
connection_message = client_sock.recv(1024)
print connection_message
to_send = 'EHLO Meow\r\n'
print to_send,
client_sock.send(to_send)
print client_sock.recv(1024)

to_send = 'STARTTLS\r\n'
print to_send,
client_sock.send(to_send)
print client_sock.recv(1024)

to_send = 'RCPT TO:<wassup@madudes.com>\r\n'
print to_send,
client_sock.send(to_send)
print client_sock.recv(1024)

to_send = 'MAIL FROM:<hello@there.com>\r\n'
print to_send,
client_sock.send(to_send)
print client_sock.recv(1024)

to_send = 'EHLO\r\n'
print to_send,
client_sock.send(to_send)
print client_sock.recv(1024)
