def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower().replace(' ', '').replace('-', '')
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True
