a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def same_elements(a,b):
    new_list = [i for i in a if i in b]
    return new_list

print(same_elements(a,b))
