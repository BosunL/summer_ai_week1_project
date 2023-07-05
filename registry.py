class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Person("John", 16)
p1.myfunc()

class Student(Person):
    def __init__(self, name, age, student_class):
        super().__init__(name, age)
        self.student_class = student_class

    def myfunc(self):
        super().myfunc()
        print("I am a student in  " + self.student_class)


p1 = Student("John", 16, "10th Grade")
p1.myfunc()