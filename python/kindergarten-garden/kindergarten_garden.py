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
        self.diagram = diagram
        self.students = students
        students.sort()


    def plants(self, student):
        i = self.students.index(student)
#         print(i)
#
#
#
# t = Garden("VVCG\nVVRC")
# print(t.plants("Bob"))
