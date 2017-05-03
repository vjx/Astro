
import socket



tsr = 'batatas e cenouras'     
tsr += ';'
host = '127.0.0.1'
port = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.send(tsr.encode())
s.send('bananas ;'.encode())

s.shutdown(0)

s.close()