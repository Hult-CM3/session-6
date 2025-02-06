import bcrypt

# Step 1: User creates a password
password = input("Enter a new password: ").encode()  # Convert to bytes
print("\nEncoded password:", password.hex())

# Step 2: Generate a salt and hash the passwopard
salt = bcrypt.gensalt()
print("\nGenerated salt:", salt)
hashed_password = bcrypt.hashpw(password, salt)
print("\nStored hashed password:", hashed_password)

# Step 3: Simulating a login attempt and check if the entered password matches the stored hash
while True:
    attempt = input("\nEnter your password again to log in: ").encode()
    if bcrypt.checkpw(attempt, hashed_password):
        print("✅ Login successful!")
        break
    else:
        print("❌ Incorrect password. Try again.")
