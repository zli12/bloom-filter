import hashlib
import re

class SpellChecker:
    def __init__(self):
        self.__filter_size = 100000000
        # Filter will all 0/False
        self.__filter = [False] * self.__filter_size
        # A list of indepedent hash functions
        self.__hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha256]

    def spell_check(self, content):
        typo_list = []
        if not isinstance(content, str):
            print('Invalid content.')
            return typo_list
        
        words = re.findall(r"[\w']+", content)

        for w in words:
            if not self.word_exists(w.lower()) and not w.isdigit():
                typo_list.append(w)
        
        return typo_list


    def reset(self, filter_size):
        if(filter_size<=0):
            print("Invalid filter size.")
            return

        self.__filter_size = filter_size
        self.__filter = [False] * filter_size

        
    def add_word_to_dictionary(self, word):
        if not isinstance(word, str):
            print('Invalid dictionary.')
            return
        
        word = word.encode()
        self.__update_filter(word)

            
    def add_dictionary(self, dictionary):
        if not isinstance(dictionary, list):
            print('Invalid dictionary.')
            return

        for word in dictionary:
            if not isinstance(word, str):
                continue
                
            self.add_word_to_dictionary(word)

            
    def word_exists(self, word):
        if not isinstance(word, str):
            return False
        
        word = word.encode()
        # Only when all hash values lead to True in the filter, we return True, any False value found will guarantee the word doesn't exist.
        for hf in self.__hash_functions:
            target_index = self.__compute_target_index(hf, word)
            if self.__filter[target_index] == False:
                return False    
            
        return True

    def __update_filter(self, word):
        for hf in self.__hash_functions:
            target_index = self.__compute_target_index(hf, word)
            self.__filter[target_index] = True


    def __compute_target_index(self, hash_func, word):
        return self.__compute_hash_val(hash_func, word) % self.__filter_size

    def __compute_hash_val(self, hash_func, word):
        return int(hash_func(word).hexdigest(),16)


    # Calculate how many filter bits have been set to True
    def get_filter_occupancy_rate(self):
        return round(self.__filter.count(True)/self.__filter_size,4)
        
        