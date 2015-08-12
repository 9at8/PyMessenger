__author__ = 'Aditya Thakral'

from socket import *
import common
import time

user = ''


def username():
    global user
    user = raw_input('Please enter your username: ')
    if user == '':
        username()
    elif len(user) < 3:
        print 'Username must be at least 4 characters long.\nTry again.\n'
        username()
    elif len(user) > 20:
        print 'Username can have a maximum size of 20 characters.\nTry again.\n'
        username()


try:
    conf = open('APPDATA/connection.config')
    det = conf.readlines()
    conf.close()
    for i in range(len(det)):
        if i == 0:
            print 'Your Username:', det[i][:-1]
        elif i == 1:
            print 'Partner\'s IP Address:', det[i][:-1]
        elif i == 2:
            print 'Partner\'s Port:', det[i][:-1]
    while True:
        choice = raw_input('Do you want to use the previous configuration? (y/n)')
        if choice.upper() == 'Y':
            user = det[0][:-1]
            ip = det[1][:-1]
            port = int(det[2][:-1])
            break
        elif choice.upper() == 'N':
            username()
            ip = common.validateip()
            port = common.port()
            det[0] = user + '\n'
            det[1] = ip + '\n'
            det[2] = str(port) + '\n'
            conf = open('APPDATA/connection.config', 'w')
            conf.writelines(det)
            conf.close()
            break
        else:
            print 'Invalid input...'
except IOError:
    det = [None, None, None]
    username()
    ip = common.validateip()
    port = common.port()
    det[0] = user + '\n'
    det[1] = ip + '\n'
    det[2] = str(port) + '\n'
    conf = open('APPDATA/connection.config', 'w')
    conf.writelines(det)
    conf.close()

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
