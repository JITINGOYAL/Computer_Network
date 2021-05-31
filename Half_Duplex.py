//server

import socket
server_port = 5000
server_socket = socket.socket()
server_socket.bind(('',server_port))
server_socket.listen(1)
print ("The server is ready!")
connection_socket, address = server_socket.accept()
while True:
  sentence = connection_socket.recv(2048).decode()
  print('>> ',sentence)
  message = input(">> ")
  connection_socket.send(message.encode())
  if(message == 'quit'):
    connection_socket.close()


//client

import socket
server_port = 5000
server_socket = socket.socket()
server_socket.bind(('',server_port))
server_socket.listen(1)
print ("The server is ready!")
connection_socket, address = server_socket.accept()
while True:
  sentence = connection_socket.recv(2048).decode()
  print('>> ',sentence)
  message = input(">> ")
  connection_socket.send(message.encode())
  if(message == 'quit'):
    connection_socket.close()
