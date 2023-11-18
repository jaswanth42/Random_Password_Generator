import random
import string

def generate_random_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length must be a positive integer.")
                continue  # Ask the user to try again
        except ValueError as e:
            print(f"Error: {e}")
            continue  # Ask the user to try again

        random_password = generate_random_password(length)
        print("Your random password is:", random_password)

        regenerate = input("Do you want to regenerate another password? (yes/no): ").lower()
        if regenerate != 'yes':
            break  # Exit the loop if the user does not want to regenerate another password

if __name__ == "__main__":
    main()
