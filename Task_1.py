text = input("Enter text: ")

dictionary = {}

words = text.split()

for i in words:
    i = i.lower()
    if i in dictionary.keys():
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)
