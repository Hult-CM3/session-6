import os
import hashlib

# Create a salt
salt = os.urandom(16)  # Generate a random 16-byte salt

# Set a password
password = "mypassword123"

# Hash the password with the salt
hashed_password = hashlib.sha256(password.encode()).hexdigest()
salted_and_hashed_password = salt.hex() + hashed_password

# Print the results
os.system('clear') # clears the terminal screen
print("Entered password length:", len(password))
print("\nSalt:", salt.hex())  # .hex() to convert salt to readable format
print("\nHashed password:", hashed_password)
print("\nHashed password length:", len(hashed_password))  # Check the length of the hashed password
print("\nSalted & hashed password:", salted_and_hashed_password)  # Combine the salt and hashed password
print("\nSalted & hashed password length:", len(salted_and_hashed_password))