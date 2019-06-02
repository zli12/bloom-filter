import random
import string
from spell_checker import SpellChecker

dictionary_file = 'data/wordlist.txt'

def generate_random_words(num=100, len=5):
    words = []
    for i in range(100):
        word = ''
        for j in range(5):
            word += random.choice(string.ascii_letters)
        words.append(word)
    return words


def read_dictionary(file_name):
    text_file = open(file_name, "r", encoding="utf8", errors="ignore")
    return text_file.read().split('\n')


def read_text_content(file_name):
    text_file = open(file_name, "r", encoding="utf8", errors="ignore")
    content = text_file.read()
    return content


def create_spell_checker(populate_dict=True):
    checker = SpellChecker()
    if populate_dict:
        checker.add_dictionary(read_dictionary(dictionary_file))

    return checker