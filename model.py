'''
Created on Nov 21, 2014

@author: ishaansutaria
'''
from resn import *
from datetime import datetime


def getFeed():
    str1 = ''
    for message in get_feed('dent'):
        str1 +=  message['message']
    return str1

def getUserUpdates(userName):
    str1 = ''
    for update in get_user_updates(userName):
        str1 += update['message']
    return str1