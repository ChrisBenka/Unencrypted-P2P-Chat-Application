
# Created by Chris Benka on 1/28/17.
# Copyright 2017 Chris Benka. All rights reserved.
#This application is a simple unecrypted peer to peer architecture (P2P)
#chat application.
#The application simply parses arguments given by the user in the temrinal
#so that the first user may act as the server abd the second user may act
#as the client. The applciation uses the select module to identify the first
#useable readbale input(standard input or socket), and either receives data
#via the socket object and prints the message to standard output or sends
#a message to the other user via the socket object.

#instruction to compile and execute program.Please note server and client
#users must be run on two different terminals.

    #Python Unecrypt.py --s
    #Python Unecrypt.py --c
#To exit program simply press #cntrl-C



import socket
import argparse
import select
import sys

argsList = sys.argv
# If the user is the server
if argsList[1] == '--s':
    #create socket object
    s = socket.socket()
    #to allow for easy reuse of port number
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #bind the server socket to any idenitfiable address, and respective port number
    s.bind(('',9997))
    #listen for up to 10 connections
    s.listen(10)
    #accept the connection
    c,addr = s.accept()
    while True:
        list_read = [c] + [sys.stdin]
        #find the first readable input object
        (readd_list,_,_) = select.select(list_read,[],[])
        for item in readd_list:
            #if the first readable input is of type connection
            if item is c:
                #recieve the message
                message = c.recv(1024)
                #print message to the screen
                print(str(message)),
                #Attempting to send a message
            elif item is sys.stdin:
                #Read standard input and send via the connection
                message = sys.stdin.readline()
                c.send(message)
    #Terminate the connection
    c.close()
# If the user is the client
elif argsList[1]== '--c':
    s = socket.socket()
    # connect
    s.connect(('',9997))
    while True:
        read_list = [s] + [sys.stdin]
        (input_list,_,_) = select.select(read_list,[],[])
        for item in input_list:
            #if first readable input is socket
            if item is s:
                #recieve message
                message = s.recv(1024)
                # print to standard output
                print(str(message)),
                #First readable input is of type standard inptu
            elif item is sys.stdin:
                #Read standard input
                message = sys.stdin.readline()
                #send message via the socket object
                s.send(message)
    #Terminate the connection
    s.close()
