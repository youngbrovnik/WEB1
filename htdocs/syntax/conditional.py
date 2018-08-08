# if condition(boolean):
#   true
user_id = input('id? ')
user_pwd = input('password? ')
'''
if user_pwd=='111111':
    print('Welcome Master!')
else:
    print('Who are you?')
'''

'''
if user_id=='egoing':
    if user_pwd=='111111':
        print('Welcome Master!')
    else:
        print('who are you?')
else:
    print('who are you?')
'''

if user_id=='egoing' and user_pwd=='111111':
    print('Welcome Master!')
else:
    print('who are you?')
