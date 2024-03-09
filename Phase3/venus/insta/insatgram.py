class InstagramUser:
    def __init__(self, user_name, user_password, user_bio):
        self.username = user_name
        self.password = user_password
        self.bio = user_bio
    def login(self, user_name, user_password):
        if(user_name == self.username and user_password == self.password):
            return "Entry allowed"
        else:
            return "Please sign up or enter correct password"

user = InstagramUser("Shukri", 12345678, "I am sharks")
# print(user.login())