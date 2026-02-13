def mergeDicts(dict1, dict2):
    for i in dict2.keys():
        if i in dict1.keys() and isinstance(dict1[i], dict) and isinstance(dict2[i], dict):
            dict2[i] = mergeDicts(dict1[i], dict2[i])
        dict1[i] = dict2[i]
    return dict1

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}} 

mergeDicts(dict_a, dict_b)

print(dict_a)