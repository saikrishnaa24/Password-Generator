
import random

def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ""

    for i in range(length):
        password += random.choice(chars)

    return password

def main():
    print("PASSWORD GENERATOR")

    while True:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Generated Password:", password)

        again = input("Do you want another password? (yes/no): ")
        if again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
