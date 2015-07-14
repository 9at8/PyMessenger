__author__ = 'Aditya Thakral'

from socket import *
import common

s = socket(AF_INET, SOCK_STREAM)
s.bind((common.validateip(), common.port()))
s.listen(5)
c, a = s.accept()

while True:
    data = c.recv(10000)
    if data:
        print data
    else:
        print "Client closed connection"
        break