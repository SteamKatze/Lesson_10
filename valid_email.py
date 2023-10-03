import re

pattern_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,6}$')
email = input("Enter your email: ")

if pattern_email.match(email):
    print("Valid email!")
else:
    print("Invalid email!")

