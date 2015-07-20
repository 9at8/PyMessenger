__author__ = 'Aditya Thakral'

from socket import *
import common
import time

user = ''


def username():
    global user
    user = raw_input('Please enter your username:')
    if user == '':
        username()
    elif len(user) < 3:
        print 'Username must be at least 4 characters long.'
        username()


username()
s = socket(AF_INET, SOCK_STREAM)
ip = common.validateip()
port = common.port()
own = socket(AF_INET, SOCK_STREAM)
try:
    own.connect((common.ownip(), port))
except:
    pass
s.connect((ip, port))
while True:
    say = raw_input('Input Text: ')
    if say == '<Exit Code 7-Alpha-Victor>':
        print 'Good bye!'
        s.send('Good bye!')
        print 'Closing in: '
        for i in range(5, 0, -1):
            print i
            time.sleep(1)
        break
    elif say == len(say) * ' ':
        continue
    else:
        s.send(user + ' : ' + say)
        try:
            own.send(user + ' : ' + say)
        except:
            pass