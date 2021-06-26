from user import User

# list of User objects that can be authenticated
users = [
	User(1, "Pratik", "789852")
]

uname_mapping = {u.uname:u for u in users}

def verify(username, password):
	user = uname_mapping.get(username, None)
	if user and user.pwd==password:
		return user

