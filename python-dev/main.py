from typing import List, Set
import math
doc_1: List = ["The", "three", "mice"]
doc_2: List = ["mice", "three", "The"]

def get_word_frequency(word_list: List):
    freq: List = []
    doc_set: Set = set(word_list)
    for word in doc_set:
        freq.append((word,word_list.count(word)))
    print(freq)
    return freq

def inner_product(L1: List, L2: List):
    sum=0
    for word, count in L1:
        for word2, count2 in L2:
            if word == word2:
                sum += count * count2
                break
    
    return sum



if __name__ == "__main__":
    w_freq = get_word_frequency(doc_1)
    w_freq_2 = get_word_frequency(doc_2)
    numerator = inner_product(w_freq, w_freq_2)
    denominator = math.sqrt(inner_product(w_freq, w_freq) * inner_product(w_freq_2, w_freq_2))
    print(math.acos(numerator/denominator))