def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    lower_book_text = text_lower(book_text)
    number_o_words = get_num_words(book_text)
    list_o_letters = make_letters(lower_book_text)
    filled_letter_dict = count_letters(list_o_letters)
    list_filled_letter_dict = list_o_dict(filled_letter_dict)
    print_report(list_filled_letter_dict, number_o_words)
    


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

def list_o_dict(filled_letter_dict):
    dict_list = []
    for entry in filled_letter_dict:
        dict = {}
        dict[entry] = filled_letter_dict[entry]
        dict_list.append(dict)
    return dict_list
        

def print_report(filled_dict, word_count):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_list = list(alphabet)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words in this document")
    for i in range(0, len(letter_list)):
        selected_dict = filled_dict[i]
        print(f"The '{letter_list[i]}' character was found {selected_dict[letter_list[i]]} number of times")
    print("--- End report ---")
    
main()