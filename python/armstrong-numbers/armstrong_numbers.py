def is_armstrong_number(number):

    pow = len(str(number))
    sum = 0

    for n in str(number):
        sum += int(n) ** pow

    return True if sum == number else False
