import os
import re
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    wds_frq = {}
    for word in re.findall(r'\w+', text):
        if word in wds_frq:
            wds_frq[word] += 1
        else:
            wds_frq[word] = 1
    return [(key, wds_frq[key]) for key in sorted(
                                            wds_frq,
                                            key=wds_frq.get,
                                            reverse=True
                                            )]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        text = load_data(filepath)
        print(get_most_frequent_words(text)[:10])
    else:
        print('\nEnter: python3 lang_frequency.py "filepath"\n')
