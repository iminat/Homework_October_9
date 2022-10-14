def merge_dict(dict1, dict2):
    for i in dict2.keys():
        dict1[i] = dict2[i]
    return dict1

dict1 = {'word': 1, 'letter': 6}
dict2 = {'sound': 3, 'sentence': 0}
print(merge_dict(dict1, dict2))

