__author__ = 'Aditya Thakral'

from socket import *
import common
import time

da_ta = common.login()
if da_ta[0]:
    user = da_ta[1]

ip = common.validateip()
port = common.port()

s = socket(AF_INET, SOCK_STREAM)
own = socket(AF_INET, SOCK_STREAM)
while True:
    try:
        own.connect((common.ownip(), port))
        break
    except:
        print 'Please run receiver first!'
        time.sleep(5)
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
