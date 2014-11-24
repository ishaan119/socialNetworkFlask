'''
Created on Nov 21, 2014

@author: ishaansutaria
'''
from datetime import datetime
from resn import *


def createUser(userData):
    try:
        print userData
        create_user('username', **userData)
        dic1 = {'username': userData['username']}
        return dic1
    except:
        return 'Unable to create user'
     
    
def loginUser(username='userNotValid',password='notFound'):
    try:
        assert check_password(username, password)
        token = login_user(username)
        dic = {'auth_token': token}
        return dic
    except:
        print 'error'
        dic = {'error':'Invalid username or password'}
        return dic
    
def logoutUser(username='Invalid'):
    try:
        print username
        logout_user(username)
        return {"logout":"True"}
    except:
        return {"logout":"False"}

def createConnection(username1,username2):
    try:
        print username1
        print username2
        create_connection(username1, username2)
        return 1
    except e:
        print e
        return 0
    
def getFreindList(username):
    try:
        list1 = []
        for friend in get_friend_list(username):
            dic = {'user':{}}
            dic['user']['username'] = friend
            list1.append(dic)
        return list1
    except:
        return 0
        
    
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
