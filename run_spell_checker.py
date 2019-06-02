from spell_checker import SpellChecker
from util import read_text_content, create_spell_checker


def spell_check():
    checker = create_spell_checker()
    content = read_text_content('data/article.txt')
    typo = checker.spell_check(content)
    print('Possible typos: ',typo)


if __name__ == "__main__":
    spell_check()        