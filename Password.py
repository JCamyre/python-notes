from getpass import getpass
userandpass = {'64361565': 'Josephhpesoj12', 'mewinwin': 'Josephhpesoj12', 'goatlover239': 'Josephhpesoj12'}

username = input('Username: ')
password = getpass('Password: ')
looped = 0
x = True
theytrying = False
while x:
    for user, pw in userandpass.items():
        if user == username and password == pw:
            print('Logging In...')
            x = False
            break
        elif theytrying:
            print('Username or password is incorrect.')
            username = input('Username: ')
            password = getpass('Password: ')
        else:
            looped += 1
            if looped == len(userandpass):
                theytrying = True

# testing return stuff.  Return makes an instance of the function equal to a value


# def oneorzero(input):
#     if input == '1':
#         return 1
#     elif input=='0':
#         return 0
#     else:
#         return 'Neither 1 or 0'
#
#
# print(oneorzero(input('1 or 0???')))
# one = oneorzero(input())
# zero = oneorzero(input())
# print(one == 1)
# print(zero == 0)

