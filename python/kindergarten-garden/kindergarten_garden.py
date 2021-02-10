class Garden:

    students = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

    seeds = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }

    def __init__(self, diagram, students=students):
        self.diagram = diagram.split("\n")
        self.students = students
        students.sort()


    def plants(self, student):
        i = (self.students.index(student) + 1) * 2
        plant_list = []

        pair1 = self.diagram[0][i-2:i]
        pair2 = self.diagram[1][i-2:i]

        for s in pair1:
            plant_list.append(self.seeds[s])

        for c in pair2:
            plant_list.append(self.seeds[c])

        return plant_list


# t = Garden("VVCCGG\nVVCCGG")
# print(t.plants("Charlie"))
