class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1    
        
        
user_1 = User("001","Angela")
user_2 = User("002","Jack")

user_1.follow(user_2)

print(f"User name: {user_1.user_name}")
print(f"ID: {user_1.id}")
print(f"Followers: {user_1.followers}")
print(f"Following: {user_1.following}")

print(f"User name: {user_2.user_name}")
print(f"ID: {user_2.id}")
print(f"Followers: {user_2.followers}")
print(f"Following: {user_2.following}")