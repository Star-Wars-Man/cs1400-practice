username = input("Enter your username: ")
is_alnum = username.isalnum()
length = len(username)

is_valid = False

if username and is_alnum and length >= 6 and length <= 12:
    is_valid = True
elif not username:
    print("Username cannot be empty")
elif not is_alnum:
    print("Username must contain only alphanumeric characters")
elif length < 6:
    print("Username must be at least 6 characters long")
elif length > 12:
    print("Username must be at most 12 characters long")
if is_valid:
    print("Username is valid")