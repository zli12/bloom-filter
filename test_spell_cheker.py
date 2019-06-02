from spell_checker import SpellChecker
from util import read_dictionary, generate_random_words, create_spell_checker
import random
import matplotlib.pyplot as plt

# Performance test for spell checker with various filter size
def spell_checker_perf_comparison():
    # Set testing parameters
    test_word_len = 5
    test_word_list_len = 1000
    base_filter_size = test_word_list_len * 100
    file_name = 'data/wordlist.txt'
    dictionary = read_dictionary(file_name)
    test_filer_sizes = [base_filter_size * pow(2,i) for i in range(6)]
    test_words = generate_random_words(test_word_len, test_word_list_len)

    # list to store perf results for plotting
    test_fp_rates = []
    test_occupancy_rates = []

    checker = create_spell_checker(populate_dict=False)

    for filter_size in test_filer_sizes:
        print('Testing spell cheker with filter size', filter_size)
        checker.reset(filter_size)
        checker.add_dictionary(dictionary)

        error_count = 0 # counter for inconsistent (false positives) results between spell checker and dictionary lookup
        for w in test_words:
            actual_res = checker.word_exists(w)
            expected_res = w in dictionary
            if actual_res != expected_res:
                error_count += 1

        error_rate = error_count/100.
        test_fp_rates.append(error_rate)
        filter_occupancy_rate = checker.get_filter_occupancy_rate()
        test_occupancy_rates.append(filter_occupancy_rate)
        print('  False positive rate', error_rate)
        print('  Filter occupancy rate', filter_occupancy_rate)

    plt.title('False positive rate vs. filter size \n 1,000 random words, length of 5 each')
    plt.plot(test_filer_sizes,test_fp_rates, label='False Positive')
    plt.plot(test_filer_sizes,test_occupancy_rates, label='Filter Occupancy')
    plt.xlabel('Filter size')
    plt.ylabel('Rate')
    plt.legend()
    plt.savefig('image/spell_cheker.jpg')
    plt.show()


def test_ad_hoc():
    file_name = 'data/wordlist.txt'
    print('Adding dictionary',file_name)
    dictionary = read_dictionary(file_name)

    checker = create_spell_checker(populate_dict=False)
    checker.add_dictionary(dictionary)

    checker.add_word_to_dictionary('abc')
    words = ['abc','AAA','ZZZ','ZBA', 'Charlie']
    for w in words:
        print('Word {} in spell cheker:\t{},\tin dictionary\t{}'.format(w,checker.word_exists(w),(w in dictionary)))
    print(checker.get_filter_occupancy_rate())


if __name__ == "__main__":
    # test_ad_hoc()
    spell_checker_perf_comparison()