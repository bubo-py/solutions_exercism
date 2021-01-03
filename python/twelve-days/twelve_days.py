def recite(start_verse, end_verse):

    lyrics = [
        "twelve Drummers Drumming,",
        "eleven Pipers Piping,",
        "ten Lords-a-Leaping,",
        "nine Ladies Dancing,",
        "eight Maids-a-Milking,",
        "seven Swans-a-Swimming,",
        "six Geese-a-Laying,",
        "five Gold Rings,",
        "four Calling Birds,",
        "three French Hens,",
        "two Turtle Doves,",
        " and a Partridge in a Pear Tree."
        ]

    def helping_recite(x):
        if x == 1:
            return "a Partridge in a Pear Tree."
        else:
            p = lyrics[-x:]
            return " ".join(p[:x - 1]) + lyrics[-1]

    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

    recited = []
    for c in range(start_verse, end_verse + 1):
        day = days[c - 1]
        recited.append(f"On the {day} day of Christmas my true love gave to me: {helping_recite(c)}")

    return recited
