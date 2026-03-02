import random

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length (minimum 4): "))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

all_characters = letters + numbers + symbols

if length < 4:
    print("Password length must be at least 4")
else:
    # Ensure at least one character from each category
    password = ""

    password += random.choice(letters)
    password += random.choice(numbers)
    password += random.choice(symbols)

    # Fill remaining length
    for i in range(length - 3):
        password += random.choice(all_characters)

    # Shuffle the password so pattern is not predictable
    password_list = list(password)
    random.shuffle(password_list)
    final_password = "".join(password_list)

    print("\nGenerated Password:", final_password)