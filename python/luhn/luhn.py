class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if self.card_num.isdigit() and len(self.card_num) > 1:
            to_check = [int(n) for n in self.card_num[-2::-2]]
            new_numbers = []
            for x in to_check:
                x = x * 2
                if x > 9:
                    x = x - 9
                new_numbers.append(x)

            the_sum = sum(new_numbers) + sum([int(n) for n in self.card_num[::-2]])
        else:
            return False

        return True if the_sum % 10 == 0 else False
