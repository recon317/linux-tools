from argparse import ArgumentParser, Namespace
import os

parser = ArgumentParser()
parser.add_argument('path', help='Input the path of desired file',type=str)
parser.add_argument('-c', '--bytes', help='print the byte counts', action='store_true')
parser.add_argument('-m', '--chars', help='print the character counts', action='store_true')
parser.add_argument('-l', '--lines', help='print the newline counts', action='store_true')
parser.add_argument('-w', '--words', help='print the words count', action='store_true')

args: Namespace = parser.parse_args()

file_path = args.path

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    return data

file = read_file(file_path)


def word_count(file, file_path):
    split_words = file.split()
    print(f"{len(split_words)} {file_path}")

def line_count(file, file_path):
    split_words = file.split('\n')
    print(f"{len(split_words)} {file_path}")

def char_count(file, file_path):
    print(f"{len(file)} {file_path}")

def byte_count(file_path):
    byte_size = os.path.getsize(file_path)
    print(f"{byte_size} {file_path}")


if args.lines:
    line_count(file, file_path)
elif args.chars:
    char_count(file, file_path)
elif args.bytes:
    byte_count(file_path)
else:
    word_count(file, file_path)