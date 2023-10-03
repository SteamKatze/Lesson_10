import re

pattern_password = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$')
password = input("Enter your password. The password must contain one uppercase letter, one lowercase letter, one digit, one symbol, and have a length of 8 to 16 characters.: ")

if pattern_password.match(password):
    print("Valid password!")
else:
    print("Invalid password! The password must contain one uppercase letter, one lowercase letter, one digit, one symbol, and have a length of 8 to 16 characters.")