__author__ = 'Aditya Thakral'

from socket import *
import common
import time

s = socket(AF_INET, SOCK_STREAM)
print common.ownip()
s.bind((common.ownip(), common.port()))
s.listen(5)
print 'Server started.'
c, a = s.accept()
print 'ok'
while True:
    data = c.recv(10000)
    if data:
        t = str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + ' - ' \
            + str(time.localtime()[1]) + '/' + str(time.localtime()[2]) + '/' + str(time.localtime()[0])
        print data, '\n', '     ', t
    else:
        print "Client closed connection..."
        print 'Closing in: '
        for i in range(5, 0, -1):
            print i
            time.sleep(1)
        break
