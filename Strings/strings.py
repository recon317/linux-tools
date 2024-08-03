import sys
from typing import List

args = sys.argv
file_path = args[1]


def read_file():
    with open(file_path, "rb") as file:
        data = file.read()
    return data


bin_data = read_file()
bin_data = bin_data


def string_search(bin_data: List[int]):
    last_char = ''
    search_output = []
    alphabet = b"abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ0123456789 "
    for i in bin_data:
        if i in alphabet:
            search_output.append(chr(i))
        elif last_char in alphabet:
            search_output.append('\n')
        last_char = i
    joined_output = ''.join(search_output)
    split_output = joined_output.split('\n')
    for item in split_output:
        if len(item) >= 3:
            print(item)





string_search(bin_data)