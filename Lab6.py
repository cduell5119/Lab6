def encode(password):
    encoded_password = ""
    for char in password:
        new_dig = int(char) + 3

        if new_dig >= 10:
            new_dig -= 10
        encoded_password += str(new_dig)
    return encoded_password
def decode(password):
    pass

if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            password = decode(password)
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')
        elif choice == 3:
            break
