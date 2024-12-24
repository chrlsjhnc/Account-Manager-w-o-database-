import string
import random

print("Welcome to Account Manager!\n")

def create(min_length=8):
    print("Create an Account:\n")
    
    #username validation
    print("- Username must contain at least 8 characters")
    print("- Username must NOT contain special symbols\n")

    while True:
        userinput = input("Enter username: ").strip()

        #length checker
        if len(userinput) < min_length:
            print(f"Username must contain at least {min_length} characters. Try again.\n")
            continue

        #check for special symbols
        if any(char in string.punctuation for char in userinput):
            print("Username must not contain any special symbols. Try again.\n")
            continue

        print("Username Valid!\n")
        break  

    #password choices
    while True:
        passwordchoice = input("Would you like to make your own password (A) or generate one (B)?: ").strip().upper()
        if passwordchoice == 'A':
            return passvalid()
        elif passwordchoice == 'B':
            return f"Generated Password: {generate()}"
        else:
            print("Invalid choice for password creation. Please enter A or B.\n")


#password generator
def generate(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    symbs = string.punctuation
    all_chars = lower + upper + nums + symbs

    while True:
        password = "".join(random.choices(all_chars, k=length))
        print(f"Generated Password: {password}")

        satisfaction = input("Are you satisfied with this password? (Y/N): ").strip().lower()

        if satisfaction == 'y':
            return password
        elif satisfaction == 'n':
            print("Generating new password...\n")
        else:
            print("Invalid input. Please enter Y or N.")


#password strength checker
def passvalid():
    print("Password MUST contain at least 12 characters.")
    print("Password should contain at least 1 special symbol (_,!,?,@,#,$,%)")
    print("Password should contain UPPERCASE letters.")
    print("Password should contain lowercase letters.")
    print("Password MUST contain at least one numeric value.\n")

    password = input("Enter password: ").strip()
    if len(password) < 12:
        return "Password MUST contain at least 12 characters."
    if not any(char.isdigit() for char in password):
        return "Password MUST contain at least one numeric value."
    if not any(char.isupper() for char in password):
        return "Password should contain UPPERCASE letters."
    if not any(char.islower() for char in password):
        return "Password should contain lowercase letters."
    if not any(char in string.punctuation for char in password):
        return "Password MUST contain at least one special symbol."

    return "Password is strong."


#main
while True:
    print("Would you like to Create an Account (A) or Log in to an existing Account (B)?")
    choice = input("Enter choice (A/B): ").strip()

    if choice == 'A' or choice == 'a':
        print(create())
        break
    elif choice == 'B' or choice == 'b':
        print("Login functionality is not implemented yet.")
        break
    else:
        print("Invalid choice. Please enter A or B.")
