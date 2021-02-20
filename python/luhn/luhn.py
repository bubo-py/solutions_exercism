class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if self.card_num.isdigit():
            to_check = [int(n) for n in self.card_num[::2]]
            new_numbers = []
            for x in to_check:
                x = x * 2
                if x > 9:
                    x = x - 9
                new_numbers.append(x)

            the_sum = sum(new_numbers) + sum([int(n) for n in self.card_num[::-2]])

        return True if the_sum % 10 == 0 else  False

# s = Luhn("4539 1488 0343 6467")
# # print(s.card_num)
# s.valid()
