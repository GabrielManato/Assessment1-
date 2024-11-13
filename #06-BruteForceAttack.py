#06-BruteForceAttack

# Define the correct password
correct_password = "12345"
# Set the maximum number of attempts
max_attempts = 5
attempts_left = max_attempts

# Keep asking the user for the password until they enter the correct one or exceed the maximum attempts
while attempts_left > 0:
    password = input(f"Enter the password (Attempts left: {attempts_left}): ")
    
    if password == correct_password:
        print("Password accepted. Access granted.")
        break  # Exit the loop if the password is correct
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print("Incorrect password. Please try again.")
        else:
            print("Incorrect password. Authorities have been alerted.")
