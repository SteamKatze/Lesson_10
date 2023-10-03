import re

pattern_mobile_phone = re.compile(r'^\+?\d{7,12}$')
mobile_phone = input("Enter your mobile phone number: ")

if pattern_mobile_phone.match(mobile_phone):
    print("Valid mobile phone number!")
else:
    print("Invalid mobile phone number!")
