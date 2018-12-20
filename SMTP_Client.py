import socket
import smtp
# Constants:
HOSTNAME_SMTP_SERVER = 'networks.cyber.org.il'
PORT_SMTP = 587


def main():
    server_ip = socket.gethostbyname(HOSTNAME_SMTP_SERVER)
    client_sock = socket.socket()
    client_sock.connect((server_ip, PORT_SMTP))
    connection_message = client_sock.recv(1024)
    # Since this is an exercise:
    print connection_message
    # OK status
    # message = raw_input('Enter your message:\n')
    client_smtp = smtp.smtp(
        client_sock, HOSTNAME_SMTP_SERVER, 'example@email.com', 'recipient@examplemail.com',
        'AGZydXN0YUBnbXguY29tAFBhc3N3b3JkMSE=', 'Subject: Oh no!\r\n'
                                                'I am now very scared because of the attack.\r\n'
                                                'Send help pls\r\n')
    # All of the 'ifs' bellow have an exception which has a status code that can be found in the
    # 'current_status_code' parameter of each instance of the handling class (empty = no errors)
    try:
        client_smtp.hello()
        client_smtp.authenticate()
        client_smtp.mail_from()
        client_smtp.recipient_to()
        client_smtp.data()
        client_smtp.send_data()
        # quit the connection
        client_smtp.quit()
    except Exception, ex:
        print 'Had an exception %s' % ex
    # close the socket
    client_sock.close()
    print 'Closed'


if __name__ == '__main__':
    main()
