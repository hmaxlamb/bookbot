def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    print(f"There are {word_count} words found")
    make_letter_dict()



def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

def get_book_text(path):
    with open(path) as f:
        return f.read()


def make_letter_dict():
    letterdict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_list = list(alphabet)
    for letter in letter_list:
        letterdict[letter] = 0
    print(letterdict)

def

main()