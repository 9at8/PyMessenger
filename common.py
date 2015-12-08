__author__ = 'Aditya Thakral'
from socket import *


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
    # return gethostbyname(gethostname())
    return [l for l in ([ip for ip in gethostbyname_ex(gethostname())[2] if not ip.startswith("127.")][:1], [
        [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]]) if
            l][0][0]


def login():
    while True:
        u = raw_input('Enter username: ')
        if u == '':
            login()
        elif len(u) < 4:
            print 'Username must be at least 4 characters long.\nTry Again.\n'
            login()
        elif len(u) > 20:
            print 'Username can have a maximum length of 20 characters.\nTryAgain.\n'
            login()
        p = raw_input('Enter password: ')
        try:
            import mysql.connector

            cnx = mysql.connector.connect(user='root', password='9at8_thakral', database='PyMessenger', host='volumio')
            q = 'select password from login where user = ' + '\'' + u + '\'' + ';'
            cursor = cnx.cursor()
            cursor.execute(q)
            for pswd in cursor:
                pass
            if p == pswd[0]:
                return (True, u)
            else:
                print 'Wrong Password!\n'
        except ImportError:
            return (False,)
        except NameError:
            print '\'' + u + '\'', 'does not exist. You need to sign-up.'
            print 'Signing up is currently not implemented.\n'


def signup():
    while True:
        import mysql.connector

        user = raw_input('Please input a username: ')
        if user == '':
            signup()
        elif len(user) < 4:
            print 'Username must be at least 4 characters long.\nTry Again.\n'
            signup()
        elif len(user) > 20:
            print 'Username can have a maximum length of 20 characters.\nTry Again.\n'
            signup()
        cnx = mysql.connector.connect(user='root', password='9at8_thakral', database='PyMessenger', host='volumio')
        q = ''
