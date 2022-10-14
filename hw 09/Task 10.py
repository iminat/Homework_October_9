def all_unique(numbers):
    set1 = set(numbers)
    if len(numbers) == len(set1):
        return 'True'
    else:
        return 'False'


numbers = '9483752'
print(all_unique(numbers))