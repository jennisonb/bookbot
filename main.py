import sys
from stats import *

def main():
    num_args = len(sys.argv)
    if num_args < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    book_contents = get_book_text(path_to_file)
    num_words = get_number_of_words(book_contents)
    the_dict = get_number_of_each_character(book_contents)
    print_report(book_contents)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()