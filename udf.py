def print_name(name):
    first_name = name.split(' ', 1)[0]
    return first_name

input = input("Enter your full name : ")

print("\nFirst Name : ", print_name(input))
