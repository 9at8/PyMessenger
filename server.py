__author__ = 'Aditya Thakral'

from socket import *
import common
import time


def server():
    s = socket(AF_INET, SOCK_STREAM)
    print 'Connect to this IP Address:', common.ownip()
    s.bind((common.ownip(), common.port()))
    s.listen(5)
    print 'Server started.'
    c, a = s.accept()
    while True:
        data = c.recv(1024 * 10)
        if data:
            t = str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + ' - ' \
                + str(time.localtime()[1]) + '/' + str(time.localtime()[2]) + '/' + str(time.localtime()[0])
            print data, '\n', '     ', t
        else:
            print "Client closed connection..."
            time.sleep(1)
            print 'Closing in: '
            for i in range(5, 0, -1):
                print i
                time.sleep(1)
            break


server()
