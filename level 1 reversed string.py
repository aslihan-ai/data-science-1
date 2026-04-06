# LEVEL 1: Reverse a string

def reverse_string(text):
    return text[::-1]  # slicing to reverse

user_input = input("Enter a string: ")
print("Reversed string:", reverse_string(user_input))
