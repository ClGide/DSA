class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return self.username



class Users:
    def __init__(self):
        self.user_list = []

    def insert(self, user):
        if type(user) != User:
            raise ValueError("the user must be of the right class")

        self.user_list.append(user)

    def search(self, username):
        if type(username) != str:
            raise ValueError("the username must be a string")

        for user in self.user_list:
            if user.username == username:
                return user

    def update(self, username, attribute, value):
        if type(username) != str or type(value) != str:
            raise ValueError("the username and the new value must be a string")
        if attribute not in ["username", "users", "email"]:
            raise ValueError("the user has only three attributes: username,"
                             " users, email. Please check your spelling")
        user = self.search(username)
        setattr(user, attribute, value)

    def list(self):
        sorted_list = sorted(self.user_list, key=lambda x: x.username)
        return sorted_list


users = Users()

gide = User("ClGide", "Gide", "gide81")
luca = User("AyloSrd", "Luca", "lucamarongiu")
amy = User("iciamyplant", "Emma", "iciamyplant")


users.insert(gide)
users.insert(luca)
users.insert(amy)
users.update('AyloSrd', 'email', 'lucamarongiu@hotmail.com')

result = users.list()
mails = [i.email for i in result]
print(mails)


"""So this is the brute force solution. Now, let's try to understand binary search trees."""
