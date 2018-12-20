import socket
from urllib2 import urlopen


class smtp:
    def __init__(self, request_socket, server_domain, client_address, recipient_address, username, message):
        self.sock = request_socket
        self.server_domain = server_domain
        self.server_ip = socket.gethostbyname(self.server_domain)
        self.client_address = client_address
        self.recipient_address = recipient_address
        self.sender_ip = urlopen('http://ip.42.pl/raw').read()
        self.message = message
        self.current_status_code = ''
        self.username = username

    def hello(self):
        self.current_status_code = ''  # reset the current status code
        to_send = 'EHLO client.example.com\r\n'
        print to_send,
        self.sock.send(to_send)
        response = self.sock.recv(1024)
        # Since this is an exercise:
        print response
        status_code = response[:3]
        if status_code == '250':
            # OK
            return True
        # Not OK
        self.current_status_code = status_code
        return False

    def authenticate(self):
        self.current_status_code = ''
        to_send = 'AUTH PLAIN {0}\r\n'.format(self.username)
        print to_send,
        self.sock.send(to_send)
        response = self.sock.recv(1024)
        # Since this is an exercise:
        print response
        status_code = response[:3]
        self.current_status_code = status_code
        return True

    def starttls(self):
        self.current_status_code = ''
        to_send = 'STARTTLS\r\n'
        print to_send,
        self.sock.send(to_send)
        response = self.sock.recv(1024)
        # Since this is an exercise:
        print response
        status_code = response[:3]
        if status_code == '220':
            # OK
            return True
        # else
        self.current_status_code = status_code
        return False

    def mail_from(self):
        self.current_status_code = ''  # reset the current status code
        to_send = 'MAIL FROM: <{0}>\r\n'.format(self.client_address)
        print to_send,
        self.sock.send(to_send)
        response = self.sock.recv(1024)
        # Since this is an exercise:
        print response
        status_code = response[:3]
        if status_code == '250':
            # OK
            return True
        # else
        self.current_status_code = status_code
        return False

    def recipient_to(self):
        self.current_status_code = ''  # reset the current status code
        to_send = 'RCPT TO:<{0}>\r\n'.format(self.recipient_address)
        print to_send,
        self.sock.send(to_send)
        response = self.sock.recv(1024)
        # Since this is an exercise:
        print response
        status_code = response[:3]
        if status_code == '250':
            # OK
            return True
        # else
        self.current_status_code = status_code
        return False

    def data(self):
        self.current_status_code = ''  # reset the current status code
        to_send = 'DATA\r\n'
        print to_send,
        self.sock.send(to_send)
        response = self.sock.recv(1024)
        # Since this is an exercise:
        print response
        status_code = response[:3]
        if status_code == '354':
            # OK
            return True
        # else
        self.current_status_code = status_code
        return False

    def send_data(self):
        self.current_status_code = ''  # reset the current status code
        to_send = self.message
        print to_send
        self.sock.send(to_send + '\r\n.\r\n')
        response = self.sock.recv(1024)
        # Since this is an exercise:
        print response
        status_code = response[:3]
        if status_code == '250':
            # OK
            return True
        # else
        self.current_status_code = status_code
        return False

    def quit(self):
        self.current_status_code = ''  # reset the current status code
        to_send = 'QUIT\r\n'
        print to_send,
        self.sock.send(to_send)
        response = self.sock.recv(1024)
        # Since this is an exercise:
        print response
        status_code = response[:3]
        if status_code == '221':
            # OK
            self.sock.close()
            return True
        # else
        self.current_status_code = status_code
        return False

