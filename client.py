__author__ = 'Aditya Thakral'

from socket import *
import common

s = socket(AF_INET, SOCK_STREAM)
s.connect((common.validateip(), common.port()))
while True:
    say = raw_input('Input Text: ')
    if say == '<Exit Code 7-Alpha-Victor>':
        print 'Good bye!'
        s.send('Good bye!')
        break
    s.send(say)