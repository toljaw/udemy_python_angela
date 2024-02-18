class User:
    def __init__(self, id, username):             #initialize attributes
        """
        :param id:
        :param username:
        """
        #attributes:
        self.id = id
        self.username = username
        self.followers = 0                      #default value set - no need to add into constructor brackets...
        self.following = 0

    #methods:                                   #methods are not inside the "init"
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "not Bond")
user_2 = User("002", "second not Bond")

user_1.follow(user_2)

print(user_2.followers)
print((user_1.following))