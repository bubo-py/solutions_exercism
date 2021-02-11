class Garden:

    # basic student group
    students = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

    # seed names reference
    seeds = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }

    # init func, setting students arg as a default student list
    def __init__(self, diagram, students=students):
        self.diagram = diagram.split("\n") # split diagram by 2 rows
        self.students = students
        # alphabetically sorting students in case of getting different list
        students.sort()


    def plants(self, student):
        # get student index from the list and multiply it so it corresponds to seeds
        i = (self.students.index(student) + 1) * 2
        plant_list = []

        # get plants from diagram using i variable
        plants = self.diagram[0][i-2:i] + self.diagram[1][i-2:i]
        for s in plants:
            plant_list.append(self.seeds[s])

        return plant_list
