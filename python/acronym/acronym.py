def abbreviate(words):
    to_replace = ["-", "_", ","]

    for c in to_replace:
        words = words.replace(c, " ")

    words = words.split()
    acronym = ""

    for w in words:
        acronym += w[0].upper()

    return acronym
