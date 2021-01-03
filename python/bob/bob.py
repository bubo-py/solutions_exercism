def response(hey_bob):
    
    if hey_bob.isupper() and hey_bob.replace(' ', '')[-1:] == '?':
        return "Calm down, I know what I'm doing!"

    if hey_bob.replace(' ', '')[-1:] == '?':
        return 'Sure.'
    
    if hey_bob.isupper():
        return 'Whoa, chill out!'

    if hey_bob.rstrip().replace(' ', '') == '':
        return "Fine. Be that way!"

    else:
        return 'Whatever.'
