def is_valid(isbn):
    isbn = isbn.replace("-", "") # remove any dashes
    # initial values
    sum = 0
    m_number = 10

    # validate the isbn length and remove 'X' character if exists
    if len(isbn) == 10 and isbn[-1] == "X":
        isbn = isbn.replace("X", "0")
        sum += 10

    # validate the isbn and calculate its components
    if len(isbn) == 10 and isbn.isdigit():
        for n in isbn:
            sum += int(n) * m_number
            m_number -= 1
    else:
        return False

    return True if sum % 11 == 0 else False
