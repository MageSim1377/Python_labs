text = input("Enter randomt text: ")

newText = ""

counter = 0
currentEl = text[0]

for i in text:
    if i == currentEl:
        counter += 1
    else:
        newText += f"{currentEl}{counter}"
        counter = 1
        currentEl = i

newText += f"{currentEl}{counter}"

print(newText)