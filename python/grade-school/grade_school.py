class School:

    def __init__(self):
        self.students = dict()

    def add_student(self, name, grade):
        self.name = name
        self.student_grade = grade
        self.students[name] = grade

    def roster(self):
        sorted_by_grade = {k: v for k, v in sorted(sorted(self.students.items()), key=lambda item: item[1])}
        return list(sorted_by_grade)

    def grade(self, grade_number):
        output = []

        for student in self.students.items():
            if student[1] == grade_number:
                output.append(student[0])

        return sorted(output)
