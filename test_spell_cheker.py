from spell_checker import SpellChecker
import random
import string
import matplotlib.pyplot as plt

def test_spell_checker_comparison():
    test_word_len = 5
    test_word_list_len = 1000
    base_filter_size = test_word_list_len * 100

    file_name = 'wordlist.txt'
    print('Adding dictionary',file_name)

    dictionary = populate_dictionary(file_name)
    test_filer_sizes = [base_filter_size * pow(2,i) for i in range(6)]
    words = generate_random_words(test_word_len, test_word_list_len)
    test_fp_rates = []
    test_occupancy_rates = []

    checker = SpellChecker()

    for filter_size in test_filer_sizes:
        print('Testing spell cheker with filter size', filter_size)
        checker.reset(filter_size)
        checker.add_dictionary(dictionary)

        error_count = 0
        for w in words:
            actual_res = checker.word_exists(w)
            expected_res = w in dictionary
            if actual_res != expected_res:
                error_count += 1
            # print('Word {} in spell cheker:\t{},\tin dictionary\t{}'.format(w,actual_res,expected_res))
        error_rate = error_count/100.
        test_fp_rates.append(error_rate)
        print('False Positive Rate', error_rate)

        filter_occupancy_rate = checker.get_filter_occupancy_rate()
        test_occupancy_rates.append(filter_occupancy_rate)

    plt.title('False positive rate vs. filter size \n 1,000 random words, length of 5 each')
    plt.plot(test_filer_sizes,test_fp_rates, label='False Positive')
    plt.plot(test_filer_sizes,test_occupancy_rates, label='Filter Occupancy')
    plt.xlabel('Filter size')
    plt.ylabel('Rate')
    plt.legend()
    plt.savefig('spell_cheker.jpg')
    plt.show()

def test_ad_hoc():
    file_name = 'wordlist.txt'
    print('Adding dictionary',file_name)

    dictionary = populate_dictionary(file_name)

    checker = SpellChecker()
    checker.add_dictionary(dictionary)

    checker.add_word_to_dictionary('abc')
    words = ['abc','AAA','ZZZ','ZBA', 'Charlie']
    for w in words:
        print('Word {} in spell cheker:\t{},\tin dictionary\t{}'.format(w,checker.word_exists(w),(w in dictionary)))
    print(checker.get_filter_occupancy_rate())

def populate_dictionary(file_name):
    text_file = open(file_name, "r", encoding="utf8", errors="ignore")
    return text_file.read().split('\n')

def generate_random_words(num=100, len=5):
    words = []
    for i in range(100):
        word = ''
        for j in range(5):
            word += random.choice(string.ascii_letters)
        words.append(word)
    return words


if __name__ == "__main__":
    # test_ad_hoc()
    test_spell_checker_comparison()