import random, string

uppercase_lst = list(string.ascii_uppercase)
lowercase_lst = list(string.ascii_lowercase)
digits_lst = list(string.digits)
special_lst = list(string.punctuation)

password_lst = list()
password = None

def intro():
    print("\n̲̅P̲̅A̲̅S̲̅S̲̅W̲̅O̲̅R̲̅D̲̅ ̲̅G̲̅E̲̅N̲̅E̲̅R̲̅A̲̅T̲̅O̲̅R\n")
    print("̲R̲e̲c̲o̲m̲m̲e̲n̲d̲e̲d̲ ̲R̲u̲l̲e̲s̲ ̲f̲o̲r̲ ̲a̲ ̲S̲e̲c̲u̲r̲e̲ ̲P̲a̲s̲s̲w̲o̲r̲d")
    print("1. At least 12 characters — the more characters, the better")
    print("2. A mixture of both uppercase and lowercase letters")
    print("3. A mixture of letters and numbers ")
    print("4. Inclusion of at least one special character, e.g., ! @ # ? ]")
    print("Note: do not use < or > in your password, as both can cause problems in Web browsers\n")
    print("--------------------------------------\n")

def main():
    print("If you would like, you can refer to the RECOMMENDED RULES above for creating your passcode.")
    print("Please enter how many uppercase letters, lowercase letters, digits and special characters you would like in your password.")

    uppercase = int(input("\nEnter number of UPPERCASE letters: "))
    password_lst = random.choices(uppercase_lst, k=uppercase)

    lowercase = int(input("\nEnter number of LOWERCASE letters: "))
    password_lst += random.choices(lowercase_lst, k=lowercase)

    number = int(input("\nEnter number of DIGITS: "))
    password_lst += random.choices(digits_lst, k=number)

    special_character = int(input("\nEnter number of SPECIAL CHARACTERS: "))
    password_lst += random.choices(special_lst, k=special_character)

    random.shuffle(password_lst)
    password = "".join(password_lst)
    print('Your password is: "' + password + '"')

intro()
main()
