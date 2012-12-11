
def letters_and_digit(str):
    if "a" <= str.lower() <= "z" or "0" <= str <= "9":
        return True
    return False

def is_valid(username, password):
    if username == password or len(password) < 8 or not letters_and_digit(password):
        return False
    else:
        return True

def main():
    username = input("user_name: ")
    password = input("password: ")
    if is_valid(username, password):
        print("Valid Password")
    else:
        print("Invalid Password")

if __name__ == '__main__':
    main()
