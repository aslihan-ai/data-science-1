# LEVEL 2: Count vowels in a string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a word or sentence: ")
print("Number of vowels:", count_vowels(user_input))
