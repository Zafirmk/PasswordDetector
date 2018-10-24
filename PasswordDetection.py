import re
Pass = raw_input("Enter Password: ")
def password_checker(Pass):
    PasswordRegex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
    X = PasswordRegex.search(Pass)
    if X == None:
        print("Invalid, Type another password")
    else:
        print("Valid password")
password_checker(Pass)
