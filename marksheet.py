class Marks:
    def __init__(self, data_file="marksheet.txt"):
        self.data_file = data_file
        self.students = []

    def load_data(self):
        with open(self.data_file, "r") as file:
            for line in file:
                name, eng, urdu, islamiat = line.strip().split(",")
                student = {'name': name, 'eng': eng, 'urdu': urdu, 'islamiat': islamiat}
                self.students.append(student)

    def save_data(self):
        with open(self.data_file, "w") as file:
            for student in self.students:
                file.write(f"{student['name']},{student['eng']},{student['urdu']},{student['islamiat']}\n")

    def add_student(self, name, eng, urdu, islamiat):
        student = {'name': name, 'eng': eng, 'urdu': urdu, 'islamiat': islamiat}
        self.students.append(student)
        self.save_data()

c = Marks()
c.load_data()
c.add_student("muntaha", "45", "55", "66")