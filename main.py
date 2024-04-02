def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    lower_book_text = text_lower(book_text)
    list_o_letters = make_letters(lower_book_text)
    filled_letter_dict = count_letters(list_o_letters)
    print(filled_letter_dict)
    


def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

def get_book_text(path):
    with open(path) as f:
        return f.read()


def make_letter_dict():
    letter_dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_list = list(alphabet)
    for letter in letter_list:
        letter_dict[letter] = 0
    return letter_dict

def text_lower(text):
    lower_text = text.lower()
    return lower_text
    

def make_letters(text):
    character_list = []
    words = text.split()
    for word in words:
        for letter in word:
            character_list.append(letter)
    return character_list

def count_letters(letters):
    letter_dict = make_letter_dict()
    keys_letter_dict = letter_dict.keys()
    for letter in letters:
        if letter in keys_letter_dict:
            letter_dict[letter] += 1
    return letter_dict   

main()