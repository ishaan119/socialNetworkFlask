from datetime import datetime

from resn import *


#Create new user
Dent = {
    'username': 'dent',
    'password': 'password',
    'first name': 'Harvey',
    'last name': 'Dent',
    'location': 'Gotham City'
}

Joker = {
    'username': 'theJoker',
    'password': 'password',
    'location': 'Unknown'
}

create_user('username', **Dent)
create_user('username', **Joker)

assert get_user('dent')['last name'] == 'Dent'

#Friends

create_connection('dent', 'theJoker')
for friend in get_friend_list('theJoker'):
    print 'In here'
    print friend + 'here'
assert 'dent' in get_friend_list('theJoker')
assert 'theJoker' in get_friend_list('dent')

delete_connection('theJoker', 'dent')
assert 'dent' not in get_friend_list('theJoker')
assert 'theJoker' not in get_friend_list('dent')

#Followers and Following

follow('dent', 'theJoker')
assert 'dent' in get_followers_list('theJoker')
assert 'theJoker' in get_following_list('dent')

unfollow('dent', 'theJoker')
assert 'dent' not in get_followers_list('theJoker')
assert 'theJoker' not in get_following_list('dent')

#Feed
create_connection('dent', 'theJoker')


update = { 
    'message': 'Why so serious?',
    'timestamp': str(datetime.now())
}

update1 = { 
    'message': 'I am ishaan',
    'timestamp': str(datetime.now())
}
new_update('theJoker', **update) #You can also use something like: new_update('theJoker', message = '...', timestamp = '...')
new_update('theJoker', **update1) #You can also use something like: new_update('theJoker', message = '...', timestamp = '...')
#assert get_feed('dent')[0]['message'] == 'Why so serious?'
print len(get_feed('dent'))
for message in get_feed('dent'):
    print message['message']
    
for update in get_user_updates('theJoker'):
    print update['message']
#Auth

assert not check_password('dent', 'wrong_password')
assert check_password('theJoker', 'password')
token = login_user('dent')
assert validate_token(token)
logout_user('dent')
assert not validate_token(token)