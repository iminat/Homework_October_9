def highest_key(my_dict):
    sorted_values = sorted(my_dict.values(), reverse = True)
    new_dict = {}
    for i in sorted_values:
        for j in my_dict.keys():
            if my_dict[j] == i:
                new_dict[j] = my_dict[j]
    print(*new_dict.keys(), sep= '=', *new_dict.values())


my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
highest_key(my_dict)

