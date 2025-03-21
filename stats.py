from curses.ascii import isalpha


def get_number_of_words(book_contents):
    return len(book_contents.split())

def get_number_of_each_character(book_contents):
    letters_obj = {}
    for letter in book_contents:
        cur_letter = letter.lower()
        if cur_letter not in letters_obj:
            letters_obj[cur_letter] = 0
        letters_obj[letter.lower()] +=1
    return letters_obj

def print_report(book_contents):
    num_words = get_number_of_words(book_contents)
    letters_dict = get_number_of_each_character(book_contents)
    sorted_dict = sorted(letters_dict.items(), key=lambda x: x[1], reverse=True)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in sorted_dict:
        if isalpha(k) == True:
            print(f"{k}: {v}")
    pass
