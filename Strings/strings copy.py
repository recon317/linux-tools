from typing import List


def read_file():
    with open("Strings/test.py", "rb") as file:
        data = file.read()
    return data


bin_data = read_file()
bin_data = bin_data[:100]


def string_search(bin_data: List[int]):
    last_ascii = False
     # set last_ascii_char to empty string
    alphabet = b"abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ0123456789 "
    for i in bin_data:
        if i in alphabet:
            if i == ' ':
                print('')
        print(chr(i),end='')


string_search(bin_data)
