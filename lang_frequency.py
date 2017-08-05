from collections import Counter
import os
import re
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read().lower()


def get_most_frequent_words(text, quantity=10):
    wds_list = []
    for word in re.findall(r'\w+', text):
        wds_list.append(word)
    wds_frq = Counter(wds_list)
    return wds_frq.most_common(quantity)


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print('\nEnter: python3 lang_frequency.py "filepath"\n')
    filepath = sys.argv[1]
    text = load_data(filepath)
    if not text:
        print('filepath does not exist')
    print(get_most_frequent_words(text))
