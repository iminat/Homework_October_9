def sort_dict_by_value(dict1, reverse):
    sorted_values = sorted(dict1.values(), reverse=reverse) #[1,4,9]
    new_dict = {}
    for i in sorted_values:
        for j in dict1.keys():
            if dict1[j] == i:
                new_dict[j] = dict1[j]
    print(new_dict)


dict1 = {'word': 6, 'letter': 9, 'sound': 4}
sort_dict_by_value(dict1, reverse=False)
sort_dict_by_value(dict1, reverse=True)
