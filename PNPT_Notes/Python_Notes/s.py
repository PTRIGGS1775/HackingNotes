#!/bin/python3

#Sockets
import socket

HOST = 'localhost'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_inet is IPV4 and SOCK STREAM is port TCP.

s.connect((HOST,PORT))


#Below establishes a connection and waits for user input.
'''
import socket


# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to a specific address and port
server_address = ('localhost', 1234)
server_socket.bind(server_address)


# Listen for incoming connections
server_socket.listen(5)


while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()


    # Receive and send data
    data = client_socket.recv(1024)
    client_socket.send(b"Received: " + data)


    # Close the client socket
    client_socket.close()
'''
