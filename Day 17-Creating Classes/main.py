class User:
    # Creating a constructor or initalizing the attribute with init function
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0 
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Arsen")

# An attribute is a variable that is associated with an object it's the one preceded by a fullstop
# Or it is something that an object has i.e seats = 5. 5 is the attribute

user_2 =User("002", "Ken")
user_1.follow(user_2)
print(user_1.id, user_1.name, user_1.followers, user_1.following)
print(user_2.id, user_2.name,user_2.followers, user_2.following)