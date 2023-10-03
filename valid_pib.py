import re

pattern_full_name = re.compile(r'^[A-ZА-Я][a-zа-я]{1,19}\s[A-ZА-Я][a-zа-я]{1,19}\s[A-ZА-Я][a-zа-я]{1,19}$')
full_name = input("Enter your full name: ")

if pattern_full_name.match(full_name):
    print("Valid full name!")
else:
    print("Invalid full name!")

