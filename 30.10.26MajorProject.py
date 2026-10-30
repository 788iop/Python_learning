class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @property
    def get_name(self):
        dict_name = {"Имя": self.name}
        return dict_name
    def get_marks(self):
        dict_marks = {"Оценки": self.marks}
        return dict_marks
    @property
    def get_average(self):
        dict_average = sum(self.marks) / len(self.marks)
        return dict_average
def make_table(students):
    students_s = sorted(students,key = lambda s: s.name)
    for s in students_s:
        yield f'{s.name:<10} Оценки: {s.marks} | Средний: {s.get_average}'
s1 = Student("Иван",[4,4,4,5])
s2 = Student("Петя",[3,4,5,4])
s3 = Student("Костя",[5,5,4,2])
for i in make_table([s1,s2,s3]):
    print(i)