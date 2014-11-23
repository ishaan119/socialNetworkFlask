'''
Created on Nov 21, 2014

@author: ishaansutaria
'''
from datetime import datetime
from resn import *


def getFeed():
    print 'IN get feed'
    dic = {'feeds':[]}
    for update in get_user_updates('theJoker'):
        
        dic['feeds'].append(update['message'])
    return dic

def getUserUpdates():
    print 'IN get user updates'
    dic = {'feeds':[]}
    for update in get_user_updates('dent'):
        
        dic['feeds'].append(update['message'])
    return dic

def getUserUpdates():
    pass