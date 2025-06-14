#password generator
import random
import string
def password_gene():
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_characters = letters + digits + symbols

    password = [
        random.choice(letters),
        random.choice(symbols),
        random.choice(digits)
    ]
   # if password < 3:
       # print(None)
    #else:
   #     print(password)

    password += random.choice(all_characters)
    random.shuffle(password)
    return ''.join(password)
print(password_gene())
