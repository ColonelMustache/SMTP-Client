import smtplib
# Constants
HOSTNAME_SMTP_SERVER = 'networks.cyber.org.il'
PORT_SMTP = 587
print 'hehe'
server = smtplib.SMTP(HOSTNAME_SMTP_SERVER, PORT_SMTP)
print 'here!'
server.login('meow', '1234')

msg = "\nHello there!"
print 'lol'
print server.sendmail("meow@meowlington.edu", "doctordoctor@doctors.org", msg)

"""
This proves the Gvahim server is very broken... 
Either that or every single explanation of SMTP I could find is flawed.
Yay.
"""
