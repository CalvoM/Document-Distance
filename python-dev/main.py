from typing import List, Set
import math
import sys


@profile
def get_file_lines(filename):
    word_list: List = []
    with open(file= filename, mode='r', encoding='windows-1252') as f:
        word_list = f.readlines()
    
    return word_list


@profile
def get_words_from_file_lines(file_lines):
    words_list: List =[]
    for line in file_lines:
        words_list += get_words_from_line(line)

    return words_list


@profile
def get_words_from_line(line: str):
    line_word_list: List = []
    word_list: List = []
    for ch in line:
        if ch.isalnum():
            word_list.append(ch)
        elif len(word_list) > 0:
            word = ''.join(word_list)
            word.lower()
            line_word_list.append(word)
            word_list = []
    return line_word_list


@profile
def get_word_frequency(word_list: List):
    freq: List = []
    doc_set: Set = set(word_list)
    for word in doc_set:
        freq.append((word,word_list.count(word)))

    return freq


@profile
def inner_product(L1: List, L2: List):
    sum=0
    for word, count in L1:
        for word2, count2 in L2:
            if word == word2:
                sum += count * count2
                break
    
    return sum

@profile
def get_degree_of_diff(f1,f2):
    numerator = inner_product(f1,f2)
    denominator = math.sqrt(inner_product(f1,f1) * inner_product(f2,f2))
    return math.acos(numerator/denominator)

if __name__ == "__main__":
    file_words : List = get_file_lines(sys.argv[1])
    file_words1 : List = get_file_lines(sys.argv[2])
    words = get_words_from_file_lines(file_words)
    words1 = get_words_from_file_lines(file_words1)
    f1 = get_word_frequency(words)
    f2 = get_word_frequency(words1)
    print(get_degree_of_diff(f1,f2))
