class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f'Ученик: {self.name}, Средний балл: {Student(self.name,self.marks).average}'
    @property
    def average(self):
        average_grade = sum(self.marks) / len(self.marks)
        return average_grade
class Excellent(Student):
    def __init__(self,name,marks,scholarship):
        super().__init__(name,marks)
        self.scholarship = scholarship
    def __str__(self):
        return f'Отличник: {self.name}, Стипендия: {self.scholarship}'
s1 = Excellent("Иван", [5, 4, 5, 5],20000)
print(s1)



class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f'Ученик: {self.name}, Средний балл: {self.average}'
    @property
    def average(self):
        average_grade = sum(self.marks) / len(self.marks)
        return average_grade
def get_best(students):
    filtered = filter(lambda s: s.average >= 4.5,students)
    names = map(lambda s: s.name,filtered)
    best = sorted(names)
    return best

s1 = Student("Иван", [5, 4, 5, 5])
s2 = Student("Марк",[4,3,2,4,4,5])
s3 = Student("Артем",[5,5,5,5,2,3,2,2])
s4 = Student("Кирилл",[4,4,5,3,4,5])
s5 = Student("Арсений",[4,3,4,2,5,5,5,5,5])
print(get_best([s1,s2,s3,s4,s5]))


def swap_case(text):
    result = []
    for letter in text:
        if letter.upper() == letter:
            result.append(letter.lower())
        else:
            result.append(letter.upper())
    return "".join(result)
print(swap_case("Hello world!"))





def get_even_numbers(numbers):
    for num in range(numbers):
        if num % 2 == 0:
            yield num 
for i in get_even_numbers(7):
    print(i)


class athlete:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    def __str__(self):
        return f'Спортсмен {self.name} бежит со скоростью {self.speed} км/ч'
print(athlete("788iop",15))




class PiggyBank:
    def __init__(self,name):
        self.name = name
        self.money = 0
    def add_coin(self,add):
        self.money += add
    @property
    def total(self):
        return self.money
p = PiggyBank("Иван")
p.add_coin(10)
p.add_coin(5)
print(p.total)



def get_evens(number):
    for i in range(number+1):
        if i % 2 == 0:
            yield(i)
for num in get_evens(7):
    print(num)



def powers_two(number):
    num = 1
    while num < number:
        yield(num)
        num = num * 2
for num in powers_two(20):
    print(num)