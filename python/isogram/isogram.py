def is_isogram(string):
    dictionary = dict()
    filtered_string = ''.join([char for char in string if char.isalpha()])
    for letter in filtered_string.lower():
        dictionary[letter] = dictionary.get(letter, 0) + 1

    for value in dictionary.values():
        if value > 1:
            return False
    else:
        return True

