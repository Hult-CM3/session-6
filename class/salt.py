import random
import string
import hashlib

salt_length = random.randint(5, 20)

salt = ''.join(random.choices(string.ascii_letters + string.digits, k=salt_length))  # Generate a random salt
password = "mypassword123"

# Hash the password with the salt
hashed_password = hashlib.sha256(password.encode()).hexdigest()
salted_and_hashed_password = salt + hashed_password

print("\nSalt:", salt)  # Convert salt to readable format
print("\nHashed password:", hashed_password)
print("\nHashed password length:", len(hashed_password))  # Check the length of the hashed password
print("\nSalted & hashed password:", salted_and_hashed_password)  # Combine the salt and hashed password
