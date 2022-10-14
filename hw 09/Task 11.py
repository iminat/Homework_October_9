num = int(input)
def all_single(numbers):
    set1 = set(numbers)
    unique = len(numbers)-len(set1)
    not_unique = len(numbers)-unique
    return not_unique

numbers = '122345'
print(all_unique(numbers))

2 4 4 5
