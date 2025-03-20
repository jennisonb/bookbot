from stats import get_number_of_words

def main():
    path_to_file = "books/frankenstein.txt"
    book_contents = get_book_text(path_to_file)
    num_words = get_number_of_words(book_contents)
    print(f"{num_words} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()