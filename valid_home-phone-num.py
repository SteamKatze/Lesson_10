import re

pattern = re.compile(r'^\d{6,10}$')

home_phone = input("Enter your home phone number: ")
result = pattern.match(home_phone)
if result:
    print("Valid home phone number!")
else:
    print("Invalid home phone number!")
