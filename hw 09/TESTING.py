import re
def get_number(number):
    if re.match(r'^\w\d\d\d\w\w\d\d\d?$', number):
        return 'Private'
    if re.match(r'^\w\w\d\d\d\d\d\d?$', number):
        return 'Taxi'
    return 'Fail'

number = input()
print(get_blabla(number))