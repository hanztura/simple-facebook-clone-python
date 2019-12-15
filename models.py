from utils import save_permanent_data


class Account:
    objects = {}

    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name
        self.friends = []

        self.objects[username] = self

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def add_friend(self, account):
        self.friends.append(account)

    def save_new_friend(self, account):
        """Add new friend to current object friends and
        save data permanently.
        """
        self.add_friend(account)

        # update friends.txt
        f1 = '{},{}'.format(self.username, account.username)
        with open('friends.txt', 'a') as f:
            f.write('\n')
            f.write(f1)
            f.write('\n')
            f.write(f2)
