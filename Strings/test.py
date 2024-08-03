alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ0123456789 "

last_char = False
last_char_ascii = ""
chars = ""

for i in alphabet:
    if last_char:
        print(last_char_ascii + i)
    else:
        print("")
    last_char_ascii = i
    last_char = True


print(chars)
