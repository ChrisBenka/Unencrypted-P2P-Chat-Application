# Unencrypted-P2P-Chat-Application
# Created by Chris Benka on 1/28/17.
# Copyright 2017 Chris Benka. All rights reserved.
This application is a simple unecrypted peer to peer architecture (P2P)
chat application.The application simply parses arguments given by the user in the temrinal#so that the first user may act as the server abd the second user may act as the client. The applciation uses the select module to identify the first useable readbale input(standard input or socket), and either receives data via the socket object and prints the message to standard output or sends a message to the other user via the socket object.
Iinstruction to compile and execute program.Please note server and client
users must be run on two different terminals.
    Python Unecrypt.py --s
    Python Unecrypt.py --c hostname
To exit program simply press #cntrl-C
