from collections import Counter
import os
from os.path import basename
import re
import sys


def load_data_in_lower_case(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read().lower()


def get_most_frequent_words(text, quantity=10):
    wds_list = [word for word in re.findall(r'\w+', text)]
    wds_frq = Counter(wds_list)
    return wds_frq.most_common(quantity)


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print('\nEnter: python3 lang_frequency.py "filepath"\n')
        sys.exit()
    filepath = sys.argv[1]
    text = load_data_in_lower_case(filepath)
    if not text:
        print('filepath does not exist')
    else:
        most_frequent_words = get_most_frequent_words(text)
        print('\nIn {} most frequent words:\n'.format(basename(filepath)))
        for (word, frequency) in most_frequent_words:
            print('  {:<10} | {}'.format(word, frequency))
        print()
