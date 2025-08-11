import random
import string

def Gen_pass(min_length, number=True, Spec_char=True):
    letter = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letter
    if number:
        characters += digits
    if Spec_char:
        characters += special

    pwd = ""
    meets_criteria = False
    has_special = False
    has_number = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if number:
            meets_criteria = meets_criteria and has_number
        if Spec_char:
            meets_criteria = meets_criteria and has_special

    return pwd

wd = Gen_pass(10)
print(wd)
