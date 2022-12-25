
name = input("Enter your name: ")
if name.isspace() or name.isdigit():
    print(input("Sorry something went wrong"))
else:
    age = input("Enter your age: ")
    if age.isspace() or age.isalpha():
        print(input("sorry something went wrong"))
    else:
        if age.isdigit():
            address = input("Enter your address:")
            if address.isspace() or address.isdigit():
                print("Sorry, something went wrong")
            else: print("Hello Ms/Mr", name, "age", age, "located in", address + ".",
                        "thanks for being one of our community\tEnjoy")
