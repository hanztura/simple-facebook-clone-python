import random
from models import Account
from utils import get_data_from_file, save_permanent_data, show_menu


# greet the user
print('Facebook - Log In or Sign Up.')

# prepare data
usernames = get_data_from_file('usernames.txt')
passwords = get_data_from_file('passwords.txt')
names = get_data_from_file('names.txt')
friends = get_data_from_file('friends.txt')

# transform friends into (adding, added) tuple
friends = [tuple(friendship.split(',')) for friendship in friends]

# instantiate accounts
accounts_data = list(zip(usernames, passwords, names))
for account in accounts_data:
    username = account[0]
    password = account[1]
    name = account[2]

    acct = Account(username, password, name)

# set friends
for f1, f2 in friends:
    f2_account = Account.objects[f2]
    Account.objects[f1].add_friend(f2_account)

# 5.b
is_exit = False
while not is_exit:
    menu_1 = {
        'a': 'Log in',
        'b': 'Create a new account',
        'c': 'Exit'
    }

    show_menu(menu_1)

    msg = 'Select action (type and enter letter): '
    user_menu_1 = input(msg)

    if user_menu_1 == 'a':
        # 5.c
        msg = 'Username: '
        input_username = input(msg)

        msg = 'Password: '
        input_password = input(msg)

        # authenticate
        account = Account.objects.get(input_username)
        if account:
            if account.password == input_password:
                print('You are logged in.')

                msg = 'Hi {}'.format(account.name)
                print(msg)

                msg = 'Welcome to Facebook'
                print(msg)

                # 5.g
                while True:
                    menu_2 = {
                        'a': 'Show friends list',
                        'b': 'Add a friend',
                        'c': 'Log out'
                    }

                    show_menu(menu_2)

                    msg = 'Select action (type and enter letter): '
                    user_menu_2 = input(msg)

                    if user_menu_2 == 'a':
                        for i, friend in enumerate(account.friends):
                            msg = '{}. {}'.format(i + 1, friend.name)
                            print(msg)

                        continue

                    elif user_menu_2 == 'b':
                        # 5.i
                        # show accounts not yet friend
                        accounts_not_friend = list(Account.objects.values())
                        accounts_not_friend.remove(account)  # remove self
                        for friend in account.friends:
                            accounts_not_friend.remove(friend)

                        for i, not_friend in enumerate(accounts_not_friend):
                            msg = '{}. {}'.format(i + 1, not_friend.name)
                            print(msg)

                        msg = ('Add friend (type number and press enter, 0 to cancel): ')
                        # check validity of input
                        while True:
                            input_add_account = input(msg)

                            try:
                                input_add_account = int(input_add_account)
                                if 0 <= input_add_account <= len(accounts_not_friend):
                                    input_add_account -= 1  # index
                                    break  # new friend id
                                else:
                                    continue  # new friend id
                            except Exception as e:
                                continue  # new friend id

                        if input_add_account == -1:  # cancel add friend
                            continue  # 5.g

                        new_friend_account = accounts_not_friend[input_add_account]
                        account.save_new_friend(new_friend_account)

                        continue  # 5.g

                    elif user_menu_2 == 'c':
                        for i in range(random.randint(3, 5)):
                            print('logging out...')

                        is_exit = True
                        print('You are logged out.')
                        break

    elif user_menu_1 == 'b':  # 5.d
        print('Add new account')
        msg = 'Name: '
        input_new_name = input(msg)

        while True:  # valid new credentials
            msg = 'Username: '
            input_new_username = input(msg)

            msg = 'Password: '
            input_new_password = input(msg)

            # check if duplicate
            if input_new_username in usernames:
                print('Username is not available.')
                continue

            else:  # not duplicate
                break

        usernames.append(input_new_username)
        save_permanent_data('usernames.txt', input_new_username)
        save_permanent_data('passwords.txt', input_new_password)
        save_permanent_data('names.txt', input_new_name)

        # create Account object
        new_account = Account(
            input_new_username, input_new_password, input_new_name)

        msg = 'Successfully created account.'
        print(msg)

        continue

    elif user_menu_1 == 'c':
        break
    else:
        continue
