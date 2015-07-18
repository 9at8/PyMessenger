__author__ = 'Aditya Thakral'
from socket import *


def validateip():
    ipadd = raw_input('Enter the IPv4 address of the computer you want to connect to: ')
    l = 0
    u = ipadd.find('.', l)
    for i in range(3):
        temp = ipadd[l:u]
        if int(temp) > 255 or int(temp) < 0:
            print 'IP Address is invalid, try again. \n'
            validateip()
        else:
            l = u + 1
            u = ipadd.find('.', l)
    return ipadd


def port():
    while True:
        try:
            p = int(raw_input('Enter a port: '))
            break
        except ValueError:
            print 'Enter integer values only.'
    if not 50000 < p < 65000:
        print 'Please enter port between 50000 and 65000. \n'
        port()
    else:
        return p


def ownip():
    ipadd = gethostbyname(gethostname())
    return ipadd