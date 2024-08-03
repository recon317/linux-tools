import sys
from typing import List

args = sys.argv
file_path = args[1]


def read_file():
    with open(file_path, "rb") as file:
        data = file.read()
    return data


bin_data = read_file()
bin_data = bin_data[:10000]


def string_search(bin_data: List[int]):
    alphabet = b"abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ0123456789 "
    for i in bin_data:
        if i in alphabet:
            if chr(i) == ' ':
                print("")
            print(chr(i), end='')


string_search(bin_data)