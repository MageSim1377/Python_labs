password = input("Enter password: ")

if len(password) < 16:
    print("Too short")
elif password.isalpha() or password.isdigit():
    print("Weak password")
else:
    print("Strong password! You're good, man! It is really good password!")
