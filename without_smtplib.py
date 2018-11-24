from socket import *
import ssl
import base64
from pip._vendor.distlib.compat import raw_input

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
    
# Send STARTTLS command to server and print server response
startTLS = "STARTTLS\r\n"
clientSocket.send(startTLS.encode('utf-8'))

recv7 = clientSocket.recv(1024)
print(recv7.decode('utf-8'))
    
#wrap socket for ssl connection, using this socket from now on instead of clientSocket
scc = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
#print("wrapped socket")

#resend helo command, as starttls makes server forget previous exchange
scc.send(heloCommand.encode())
recv10 = scc.recv(1024).decode()
print(recv10)
    
#test gmail made for assignment, feel free to login and test
username = '<#####@#####.com>'
password = '##########'

#auth plain command requires base64 encoded user and pass in header
base64_str = ("\x00"+username+"\x00"+password).encode('utf-8')
base64_str = base64.b64encode(base64_str)
    
#do auth login
authLogin = "AUTH PLAIN ".encode('utf-8')+base64_str+"\r\n".encode('utf-8')
scc.send(authLogin)
recv9 = scc.recv(1024)
print(recv9.decode('utf-8'))

# Send MAIL FROM command and print server response.
mailFrom = 'MAIL FROM:<#####@#####.com>\r\n'
scc.send(mailFrom.encode('utf-8'))
recv2 = scc.recv(1024)
print(recv2.decode('utf-8'))
    

# Send RCPT TO command and print server response.
rcpttoCommand = 'RCPT TO:<#####@#####.com>\r\n'
scc.send(rcpttoCommand.encode('utf-8'))
recv3 = scc.recv(1024)
print(recv3.decode('utf-8'))


# Send DATA command and print server response.
data = 'Data\r\n'
scc.send(data.encode('utf-8'))
recv4 = scc.recv(1024)
print(recv4.decode('utf-8'))

# Send message data.
message = raw_input('Enter Message Here: ')

# Message ends with a single period.
messageEnd = '\r\n.\r\n'
scc.send((message + messageEnd).encode('utf-8'))
recv5 = scc.recv(1024)
print(recv5.decode('utf-8'))

# Send QUIT command and get server response.
quitMes = 'Quit\r\n'
print(quitMes)
scc.send(quitMes.encode('utf-8'))
recv6 = scc.recv(1024)
print(recv6.decode('utf-8'))

#close socket connection
scc.close()