import socket
import smtp
# Constants:
HOSTNAME_SMTP_SERVER = 'networks.cyber.org.il'
PORT_SMTP = 587


def main():
    while True:
        server_ip = socket.gethostbyname(HOSTNAME_SMTP_SERVER)
        client_sock = socket.socket()
        client_sock.connect((server_ip, PORT_SMTP))
        connection_message = client_sock.recv(1024)
        # Since this is an exercise:
        print connection_message
        status_code = connection_message[:3]
        if status_code == '220':
            # OK status
            # message = raw_input('Enter your message:\n')
            client_smtp = smtp.smtp(client_sock, HOSTNAME_SMTP_SERVER, 'example@email.com', 'recipient@examplemail.com',
                                    'hello')
            # All of the 'ifs' bellow have an exception which has a status code that can be found in the
            # 'current_status_code' parameter of each instance of the handling class (empty = no errors)
            if client_smtp.hello():
                """
                if client_smtp.authenticate():
                    if client_smtp.starttls():
                        if client_smtp.mail_from():
                            if client_smtp.recipient_to():
                                if client_smtp.data():
                                    if client_smtp.send_data():
                                        if client_smtp.quit():
                                            print 'Message sent, disconnected...\n'
                """
            if raw_input('===\n').upper() == 'EXIT':
                break
        else:
            print 'The mail service is not available at this time\nClosing the connection...'
            client_sock.close()
            break
    print 'Closed'


if __name__ == '__main__':
    main()
