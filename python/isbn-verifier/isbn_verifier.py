def is_valid(isbn):
    isbn = isbn.replace("-", "")
    sum = 0
    m_number = 10

    if len(isbn) == 10 and isbn[-1] == "X":
        isbn = isbn.replace("X", "0")
        sum += 10

    if len(isbn) == 10 and isbn.isdigit():

        for n in isbn:
            sum += int(n) * m_number
            m_number -= 1

    else:
        return False

    return True if sum % 11 == 0 else False

print(is_valid("359821507X"))
