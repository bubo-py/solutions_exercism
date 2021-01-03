class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(n) for n in numbers.split()] for numbers in matrix_string.split('\n')]
        
    def row(self, index):
        self.result = []
        for selected_row in self.matrix:
            self.result.append(selected_row)
        return self.result[index - 1]

    def column(self, index):
        self.result = []
        self.result2 = []
        for selected_column in self.matrix:
            self.result.append(selected_column)
        for selected_col in self.result:
            self.result2.append(selected_col[index-1])

        return self.result2
