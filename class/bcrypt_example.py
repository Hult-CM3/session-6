import bcrypt

password = input("please enter a pasword: ").encode()

# Generate a salt and hash the password
salt = bcrypt_example.gensalt()
hashed_password = bcrypt_example.hashpw(password, salt)

print("Salted & hashed password:", hashed_password)