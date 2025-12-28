import string
import copy


def count_words(strToCheck):
    if not isinstance(strToCheck, str):
        raise TypeError("Incorrecr type!")
    clearStr = strToCheck.strip()
    if len(clearStr) == 0:
        return 0
    return len(clearStr.split(' '))

def find_unique(listToCHeck):
    if not isinstance(listToCHeck, list):
        raise TypeError("Incorrecr type!")
    unique = []
    for i in listToCHeck:
        if not i in unique:
            unique.append(i)
    return unique

def is_palindrome(strToCheck):
    if not isinstance(strToCheck, (int, str)):
        raise TypeError("Incorrecr type!")
    newStr = str(strToCheck)
    while len(newStr) > 1:
        if newStr[0] != newStr[-1]:
            return False
        newStr = newStr[1: -1]
    return True

def are_anagrams(word1, word2):
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Incorrecr type!")
    letters1 = []
    letters2 = []

    letters1.extend(word1.lower())
    letters2.extend(word2.lower())

    for i in range(len(letters1)):
        for j in range(len(letters1) - 1):
            if letters1[j] < letters1[j + 1]:
                t = letters1[j]
                letters1[j] = letters1[j + 1]
                letters1[j + 1] = t

    for i in range(len(letters2)):
        for j in range(len(letters2) - 1):
            if letters2[j] < letters2[j + 1]:
                t = letters2[j]
                letters2[j] = letters2[j + 1]
                letters2[j + 1] = t

    flag = True

    if len(letters1) != len(letters2):
        flag = False
    else:
        for i in range(len(letters1)):
            if letters1[i] != letters2[i]:
                flag = False
                break
    return flag


def mergeDicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Incorrecr type!")
    newDict = copy.deepcopy(dict1)
    for i in dict2.keys():
        if i in dict1.keys() and isinstance(dict1[i], dict) and isinstance(dict2[i], dict):
            newDict[i] = mergeDicts(dict1[i], dict2[i])
        else:
            newDict[i] = dict2[i]
    return newDict

