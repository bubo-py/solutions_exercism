import re

def count_words(sentence):
    pattern = re.compile(r"[a-z0-9']+")
    matches = pattern.findall(sentence.lower())
    counted = dict()

    for word in matches:
        word = word.strip("'")
        counted[word] = counted.get(word, 0) + 1

    return counted
