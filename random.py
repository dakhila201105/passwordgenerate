import string
import random
def creating_password(length, desired_digits, desired_punc):
    digits = string.digits
    punc = string.punctuation
    letters = string.ascii_letters
    all_characters = letters + digits + punc
    list_1= []
    for i in desired_digits:
        if str(i) in digits:
            list_1.append(str(i))
    list_2 = []
    for i in desired_punc:
        if str(i) in punc:
            list_2.append(str(i))
    password_chars = list_1 + list_2
    if len(password_chars) < length:
        password_chars += random.choices(all_characters, k=length-len(password_chars))
        random.shuffle(password_chars)
    password = ''.join(password_chars)
    return password
def exceptions():
    try:
        length = int(input("Enter the length of the password: "))
        if length < 10:
            raise ValueError("The length must be above 10. Enter a valid length.")
    except Exception as ex:
        print("An unexpected exception occurred: ", ex)
    desired_digits = list(input("Enter the desired digits: "))
    desired_punc = list(input("Enter the desired punctuations: "))
    password = creating_password(length, desired_digits, desired_punc)
    print(password)
exceptions()
