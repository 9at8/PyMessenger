__author__ = 'Aditya Thakral'
from socket import *

__login = []


def validateip():
    ipadd = raw_input('Enter the IPv4 address of the computer you want to connect to: ')
    l = 0
    u = ipadd.find('.', l)
    for i in range(3):
        try:
            temp = int(ipadd[l:u])
            if temp > 255 or temp < 0:
                print 'IP Address is invalid, try again. \n'
                validateip()
            else:
                l = u + 1
                if i != 2:
                    u = ipadd.find('.', l)
                else:
                    u = None
                    try:
                        temp = int(ipadd[l:u])
                        if temp > 255 or temp < 0:
                            print 'IP Address is invalid, try again. \n'
                            validateip()
                    except ValueError:
                        print 'IP Address is invalid, try again. \n'
                        validateip()
        except ValueError:
            print 'IP Address is invalid, try again. \n'
            validateip()
    return ipadd


def port():
    while True:
        try:
            p = int(raw_input('Enter a port: '))
            break
        except ValueError:
            print 'Enter integer values only.'
    if not 20000 < p < 40000:
        print 'Please enter port between 20000 and 40000. \n'
        port()
    else:
        return p


def ownip():
    return gethostbyname(gethostname())


def login():
    if __login == []:
        user = raw_input('Enter Username: ')
        password = raw_input('Enter Password: ')
        __login.append(user)
        __login.append(password)

