# you might need to run "pip install bcrypt" in your terminal before this will work
import bcrypt

password = input("please enter a pasword: ").encode()

# Generate a salt and hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

print("Salted & hashed password:", hashed_password)