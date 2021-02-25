class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        # simple validation if given input is possible to process
        if self.card_num.isdigit() and len(self.card_num) > 1:
            # looping through every 2 number, starting from second last one
            to_check = [int(n) for n in self.card_num[-2::-2]]
            new_numbers = []

            for x in to_check:
                x = x * 2
                if x > 9:
                    x = x - 9
                new_numbers.append(x)

            # sum of the doubled numbers and the rest
            the_sum = sum(new_numbers) + sum([int(n) for n in self.card_num[::-2]])
        else:
            return False

        return True if the_sum % 10 == 0 else False
